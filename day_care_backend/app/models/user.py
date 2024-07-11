#!/usr/bin/python3

from . import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    
    payments = db.relationship('Payment', back_populates='user', lazy=True)
    
def to_dict(self):
    return {
        'user_id': self.user_id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'email': self.email,
        'role': self.role
    }
User.to_dict = to_dict