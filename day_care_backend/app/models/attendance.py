#!/usr/bin/python3

from . import db 

class Attendance(db.Model):
    attendance_id = db.Column(db.Integer, primary_key=True)
    present_status = db.Column(db.Boolean)
    date = db.Column(db.Date)
    child_id = db.Column(db.Integer, db.ForeignKey('child.child_id'))
    class_id = db.Column(db.Integer, db.ForeignKey('classroom.class_id'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))

    child = db.relationship('Child', back_populates='attendances')
    classroom = db.relationship('Classroom', back_populates='attendances')
    staff = db.relationship('Staff', back_populates='attendances')

def to_dict(self):
    return {
        'attendance_id': self.attendance_id,
        'child_id': self.child_id,
        'class_id': self.class_id,
        'present_status': self.present_status,
    }
Attendance.to_dict = to_dict