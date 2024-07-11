#!/usr/bin/python3

from . import db

class Activity(db.Model):
    activity_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text)
    age_group = db.Column(db.String(50))
    scheduled_for = db.Column(db.DateTime)

def to_dict(self):
    return {
        'activity_id': self.activity_id,
        'name': self.name,
        'description': self.description,
        'age_group': self.age_group,
        'scheduled_for': self.scheduled_for.strftime('%Y-%m-%d %H:%M:%S')
    }
Activity.to_dict = to_dict