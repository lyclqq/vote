from flask import Blueprint,render_template,current_app,url_for,redirect,session,request,flash
from ext import db
from common import wapper,cvote
from form.createvote import Createvote

admin_con=Blueprint('admin',__name__)

@admin_con.route('/create_vote',methods=['POST','GET'],endpoint='create_vote')
@wapper
def createvote():
    username=session.get('username')
    usertype=session.get('usertype')
    form=Createvote()
    if request.method=='POST':
        if request.form.get('types')=="生成投票":
            if cvote():
                flash("成功")
            else:
                flash("失败")
    return render_template('createvote.html',username=username,usertype=usertype,form=form)