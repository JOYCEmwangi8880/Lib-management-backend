from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Book(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False) 
    stock = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'stock': self.stock,
        }

class Member(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    debt = db.Column(db.Float, default=0)

   

class Transaction(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    date_issued = db.Column(db.DateTime, nullable=False)
    date_returned = db.Column(db.DateTime, nullable=True)
    rentfee = db.Column(db.Float, default=0)

    