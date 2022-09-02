from ext import db
from sqlalchemy.sql import func

class Vote(db.Model):
    __tablename__='votes'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    score=db.Column(db.Integer,default=0)
    status=db.Column(db.Integer)
    users_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    article_id = db.Column(db.Integer, db.ForeignKey("articles.id"))