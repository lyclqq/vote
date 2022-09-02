from flask import Blueprint,render_template,current_app,url_for,redirect,session,request
from ext import db
from common import wapper
from model.user import Users
from model.articles import Articles
from model.vote import  Vote
from form.article import PostForm
from form.score import ScoreadminForm
from sqlalchemy import func
from operator import and_
article_con=Blueprint('article',__name__)


@article_con.route('/articlevoteshow/<aid>',endpoint='articlevoteshow')
@wapper
def articlevoteshow(aid):
    username=session.get('username')
    usertype=session.get('usertype')
    result=db.session.query(Vote).filter(and_(Vote.article_id==aid,Articles.id==Vote.article_id)).all()
    return render_template('articlevoteshow.html',usertype=usertype,username=username,result=result)

@article_con.route('/articleadmin',endpoint='articleadmin')
@wapper
def articleadmin():
    username=session.get('username')
    usertype=session.get('usertype')
    result=db.session.query(Articles).all()
    return render_template('articleadmin.html',usertype=usertype,username=username,result=result)

@article_con.route('/articlecreate',endpoint='articlecreate')
def articlecreate():
    username=session.get('username')
    usertype=session.get('usertype')
    form=PostForm()
    return render_template('createarticle.html',usertype=usertype,username=username,form=form)

@article_con.route('/scoreadmin',methods=['POST','GET'],endpoint='scoreadmin')
@wapper
def scoreadmin():
    username=session.get('username')
    usertype=session.get('usertype')
    form =ScoreadminForm()
    result=db.session.query(Articles).order_by('id').all()
    if request.method=='POST':
        for item in result:
            item.score1=round(db.session.query(func.avg(Vote.score)).filter(and_(Vote.status==1,item.id==Vote.article_id)).scalar())
            print('s1=',item.score1)
            item.score2 = round(db.session.query(func.avg(Vote.score)).filter(
                and_(Vote.status == 2, item.id == Vote.article_id)).scalar())
            print('s2=', item.score2)
            item.score=float(item.score1)*0.6+float(item.score2)*0.4
            print('score=', item.score)
        db.session.commit()
    return render_template('scoreadmin.html',username=username,usertype=usertype,result=result,form=form)