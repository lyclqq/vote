from flask import Blueprint,render_template,current_app,url_for,redirect,session,request
from ext import db
from form.user import UserForm
from model.user import Users
user_con=Blueprint('user',__name__)
from model.user import Users
from model.vote import Vote
from model.articles import Articles
import random
from common import wapper
from operator import and_

@user_con.route('/userdelete/<uid>',endpoint='userdelete')
@wapper
def userdelete(uid):
    username=session.get('username')
    usertype=session.get('usertype')
    db.session.query(Vote).filter(Vote.users_id==uid).delete()
    db.session.query(Users).filter(Users.id==uid).delete()
    db.session.commit()
    result=db.session.query(Users).all()
    return render_template('useradmin.html',username=username,usertype=usertype,result=result)

@user_con.route('/uservoteshow/<uid>',endpoint='uservoteshow')
@wapper
def uservoteshow(uid):
    username=session.get('username')
    usertype=session.get('usertype')
    result=db.session.query(Vote).filter(and_(Vote.article_id==Articles.id,Vote.users_id==uid)).all()
    return render_template('uservoteshow.html',username=username,usertype=usertype,result=result)

@user_con.route('/pwd/<uid>',endpoint='pwd')
@wapper
def pwd(uid):
    username=session.get('username')
    usertype=session.get('usertype')
    user=db.session.query(Users).filter(Users.id==uid).first()
    user.password=str(random.randint(100000,999999))
    db.session.commit()
    result=db.session.query(Users).all()
    return render_template('useradmin.html',username=username,usertype=usertype,result=result)

@user_con.route('/useradmin',endpoint='useradmin')
@wapper
def useradmin():
    username=session.get('username')
    usertype=session.get('usertype')
    result=db.session.query(Users).all()
    return render_template('useradmin.html',username=username,usertype=usertype,result=result)

@user_con.route('/usercreate',methods=['GET','POST'],endpoint='usercreate')
@wapper
def usercreate():
    username=session.get('username')
    usertype=session.get('usertype')
    form=UserForm()
    if request.method =='POST':
        uname=request.form.get('username')
        utype=request.form.get('usertype')
        user=Users()
        user.username=uname
        user.usertype=utype
        user.password=str(random.randint(100000,999999))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.useradmin'))
    else:
        return render_template('createuser.html',username=username,usertype=usertype,form=form)