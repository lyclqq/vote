from ext import db
from sqlalchemy.sql import func

class Articles(db.Model):
    __tablename__='articles'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(250),nullable=False)
    titlelink=db.Column(db.String(200))
    pubdate=db.Column(db.Date)
    author = db.Column(db.String(100))
    content=db.Column(db.Text)
    types=db.Column(db.String(100))
    clicks=db.Column(db.Integer,default=0)
    titlejpg=db.Column(db.String(100))
    updatedate=db.Column(db.DateTime,default=func.now())
    cause=db.Column(db.Text)
    score1=db.Column(db.Float,default=0)
    score2=db.Column(db.Float,default=0)
    score=db.Column(db.Float,default=0)
    votes=db.relationship("Vote",backref="article")
