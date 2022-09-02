import random
import string
from PIL import Image,ImageFont,ImageDraw
from ext import db
from model.user import Users
from model.articles import Articles
from model.vote import Vote

from flask import session,current_app,redirect
import datetime

def getKey():
    return ''.join(random.sample(string.digits,4))

def rndColor():
    return (random.randint(16,128),random.randint(16,128),random.randint(16,128))

def getVerifyCode(imgKey):
    width,height=120,50
    im=Image.new('RGB',(width,height),'white')
    font= ImageFont.truetype('arial', 40)
    draw=ImageDraw.Draw(im)
    for item in range(4):
        draw.text((5+random.randint(-3,3)+23*item,5+random.randint(-3,3)),text=imgKey[item],fill=rndColor(),font=font)
    return im

def userLogin(username,password):
    user=db.session.query(Users).filter(Users.username==username).first()
    if user is None:
        return False
    if user.password==password:
        session.permanent=True
        current_app.permanent_session_lifetime=datetime.timedelta(seconds=3600)
        session['username']=user.username
        session['usertype']=user.usertype
        user.cdate=datetime.datetime.now()
        db.session.commit()
        return True
    else:
        return False


def wapper(func):
    def inner(*args,**kwargs):
        if not session.get('username'):
            return redirect('/login')
        return func(*args,**kwargs)
    return inner

def cvote():
    users=Users.query.all()
    articles=Articles.query.all()
    for user in users:
        for article in articles:
            vote=Vote()
            vote.article_id=article.id
            vote.users_id=user.id
            vote.score=60
            if user.usertype=="admin":
                vote.status=0
            elif user.usertype=="user2":
                vote.status=2
            else:
                vote.status=1
            db.session.add(vote)
    db.session.commit()
    return True