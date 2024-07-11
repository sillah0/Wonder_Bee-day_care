#!/usr/bin/python3

from . import db

class Parent(db.Model):
    parent_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    address = db.Column(db.String(50))
    contacts = db.Column(db.Integer)
    reg_status = db.Column(db.String(50))

    user = db.relationship('User', backref='parent')
    children = db.relationship('Child', back_populates='parent')

def to_dict(self):
    return {
        'parent_id': self.parent_id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'address': self.address,
        'contacts': self.contacts
    }
Parent.to_dict = to_dict