from ext import db
from sqlalchemy.sql import func

class Users(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(20))
    usertype=db.Column(db.String(20))
    cdate=db.Column(db.DateTime,default=func.now())
    votes=db.relationship("Vote",backref="user")




