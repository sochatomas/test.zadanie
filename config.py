from flask import Flask
from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
db = SQLAlchemy(app)

post_args = reqparse.RequestParser()
post_args.add_argument("userId", type=int, required=True)
post_args.add_argument("title", type=str, required=True)
post_args.add_argument("body", type=str, required=True)
post_args.add_argument("id", type=str)


update_post_args = reqparse.RequestParser()
update_post_args.add_argument("title", type=str)
update_post_args.add_argument("body", type=str)
