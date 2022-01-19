from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String 
from dateTime import datetime

from portfolium import db, login_manager 


class ChangeModels(db.Model):
	id          		= db.Column(db.Integer,primary_key=True)
    received_currency	= db.Column(db.String(50),nullable=False)
    return_currency		= db.Column(db.String(50),nullable=False)
    received_nominal	= db.Column(db.String(250),nullable=False)
    return_nominal		= db.Column(db.String(250),nullable=False)
    date 				= db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ChangeModels {self.id}>"

