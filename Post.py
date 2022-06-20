from config import *


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    userId = db.Column(db.Integer)
    title = db.Column(db.String)
    body = db.Column(db.String)

    def __init__(self,id, userId, title, body):
        self.id = id
        self.userId = userId
        self.title = title
        self.body = body
