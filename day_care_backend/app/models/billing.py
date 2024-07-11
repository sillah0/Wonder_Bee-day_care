#!/usr/bin/python3

from . import db

class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(50), nullable=False)
    
    user = db.relationship('User', backref=db.backref('payments', lazy=True))
    
def to_dict(self):
    return {
        'payment_id': self.payment_id,
        'user_id': self.user_id,
        'amount': self.amount,
        'status': self.status,
        'created_at': self.created_at
    }
    