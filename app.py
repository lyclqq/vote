#coding=utf-8

from flask import Flask,render_template,url_for,redirect,make_response,session,request,flash,send_from_directory,g
from ext import db
from  model.vote import Vote
from model.articles import Articles
from model.user import Users
from form.login import LoginForm
import random
from flask_wtf.csrf import CSRFProtect
from common import getKey,getVerifyCode,userLogin,wapper
from io import BytesIO
from flask_ckeditor import CKEditor,CKEditorField,upload_fail,upload_success
import datetime
import os
from operator import and_,or_
from form.score import ScoreForm

app=Flask(__name__)
app.config.from_pyfile("config.py")
db.app=app
db.init_app(app=app)
csrf=CSRFProtect(app)
ckeditor=CKEditor(app)

@app.before_request
def before_request():
    if session.get("username"):
        g.uname=session.get("username")
        g.utype=session.get("usertype")

@app.route('/default',endpoint='default')
@wapper
def default():
    username=session.get("username")
    user=db.session.query(Users).filter(Users.username==username).first()
    rs=db.session.query(Vote).filter(and_(Vote.article_id==Articles.id,Vote.users_id==user.id)).all()
    return render_template('default.html',result=rs)

@app.route('/uservote/<int:aid>',methods=['GET','POST'],endpoint='uservote')
@wapper
def uservote(aid):
    username=session.get('username')
    usertype=session.get('usertype')
    form=ScoreForm()
    post=db.session.query(Vote).filter(and_(Vote.article_id==Articles.id,Vote.id==aid)).first()
    if request.method=='POST' and form.validate():
        score=request.form.get('score')
        post.score=score
        db.session.commit()
        return redirect(url_for('default'))
    else:
        form.score.data=post.score
    return render_template('score.html',usertype=usertype,username=username,item=post,form=form)

@app.errorhandler(404)
def error_404(arg):
    return 'this is null!'

@app.route('/upload',methods=['POST'],endpoint='upload')
def upload():
    f=request.files.get('upload')
    extension=f.filename.splist('.')[-1].lower()
    if extension not in ['jpg','gif','png','jpeg']:
        return upload_fail(message='只能上传图片')
    newfilename=session.get('username')+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    f.save(os.path.join(app.config['UPLOADED_PATH'],newfilename+'.'+extension))
    url=url_for('uploaded_files',filename=newfilename+'.'+extension)
    return upload_success(url=url)

@app.route('/files/<filename>')
def uploaded_files(filename):
    path=app.config['UPLOADED_PATH']
    return send_from_directory(path,filename)

@app.route('/admin')
@wapper
def admin():

    return 'this is admin'

@app.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    if request.method=='POST':
        verifycode=request.form.get('verify_code')
        username=request.form.get('username')
        password=request.form.get('password')
        if session['imageCode']==verifycode:
            if userLogin(username,password)==True:
                return redirect(url_for('default'))
            else:
                flash('用户名或密码错误！')
                return render_template('login.html', form=form)
        else:
            flash('验证码错误！')
            return render_template('login.html', form=form)
    else:
        return render_template('login.html',form=form)

@app.route('/temp')
def temp():
    tom=db.session.query(Users).filter(Users.username=='tom').first()
    db.session.delete(tom)
    db.session.commit()
    return 'OK'

@app.cli.command()
def createdata():
    db.drop_all()
    db.create_all()

@app.route('/imgCode')
def imgcode():
    imgKey=getKey()
    image=getVerifyCode(imgKey)
    buf=BytesIO()
    image.save(buf,'jpeg')
    buf_str=buf.getvalue()
    response=make_response(buf_str)
    response.headers['Content-Type']='image/gif'
    session['imageCode']=imgKey
    return response

@app.cli.command()
def insdb():
    user=Users()
    user.username='admin'
    user.usertype='admin'
    user.password=str(random.randint(100000,999999))
    db.session.add(user)
    article1=Articles()
    article2=Articles()
    article3=Articles()
    article1.title='title1'
    article2.title='title2'
    article3.title='title3'
    db.session.add(article1)
    db.session.add(article2)
    db.session.add(article3)
    vote=Vote()
    vote.article=article1
    vote.user=user
    db.session.add(vote)
    db.session.commit()

if __name__=='__main__':
    from control.user import *
    from control.article import *
    from control.admin import *
    app.register_blueprint(user_con,url_prefix='/user')
    app.register_blueprint(article_con, url_prefix='/article')
    app.register_blueprint(admin_con, url_prefix='/admin')
    app.run('0.0.0.0',port=80,debug=True)