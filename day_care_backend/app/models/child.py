#!/usr/bin/python3

from . import db

class Child(db.Model):
    child_id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.parent_id'))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    med_cond =db.Column(db.String(50))

    parent = db.relationship('Parent', back_populates='children')
    enrollments = db.relationship('Enrollment', back_populates='child')
    attendances = db.relationship('Attendance', back_populates='child')
    
