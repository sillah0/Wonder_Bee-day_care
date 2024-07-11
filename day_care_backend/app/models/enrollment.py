#!/usr/bin/python3

from . import db

class Enrollment(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child.child_id'))
    class_id = db.Column(db.Integer, db.ForeignKey('classroom.class_id'))

    child = db.relationship('Child', back_populates='enrollments')
    classroom = db.relationship('Classroom', back_populates='enrollments')

def to_dict(self):
    return {
        "enrollment_id": self.enrollment_id,
        "child_id": self.child_id,
        "class_id": self.class_id,
        "date_enrolled": self.date_enrolled
    }
Enrollment.to_dict = to_dict
