#!/usr/bin/python3

from . import db

class Classroom(db.Model):
    class_id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))
    class_name = db.Column(db.String(50), nullable=False)

    teacher = db.relationship('Staff', back_populates='classroom')
    enrollments = db.relationship('Enrollment', back_populates='classroom')
    attendances = db.relationship('Attendance', back_populates='classroom')
    
def to_dict(self):
    return {
        'class_id': self.class_id,
        'teacher_id': self.teacher_id,
        'class_name': self.class_name
        }
Classroom.to_dict = to_dict