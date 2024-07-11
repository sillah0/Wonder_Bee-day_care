#!/usr/bin/python3
from . import db 

class Staff(db.Model):
    staff_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    position = db.Column(db.String(50))

    user = db.relationship('User', backref='staff')
    classroom = db.relationship('Classroom', back_populates='teacher')
    attendances = db.relationship('Attendance', back_populates='staff')

def to_dict(self):
    return {
        "staff_id": self.staff_id,
        "first_name": self.first_name,
        "last_name": self.last_name,
        "position": self.position,
        "contacts": self.contacts
    }
Staff.to_dict = to_dict