#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Activity, User
from datetime import datetime 

activity = Blueprint('activity', __name__)

@activity.route('/', methods=['GET'])
@jwt_required()
def get_all_activities():
    activities =  Activity.query.all()
    return jsonify([activity.to_dict() for activity in activities]), 200

@activity.route('/<int:activity_id>', methods=['GET', 'PUT','DELETE'])
@jwt_required()
def activity_operations(activity_id):
    activity_record = Activity.query.get_or_404(activity_id)
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role not in ['staff', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 403
    if request.method == 'GET':
        return jsonify(activity_record.to_dict()), 200
    elif request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(activity_record, key, value)
        db.session.commit()
        return jsonify({"message": "Activity updated successfully"}), 200
    elif request.method == 'DELETE':
        db.session.delete(activity_record)
        db.session.commit()
        return jsonify({"message": "Activity Deleted"}), 200

@activity.route('/create', methods=['POST'])
@jwt_required()
def create_activity():
    data = request.get_json()
    new_activity = Activity(
        name=data['name'],
        description=data['description'],
        age_group=data['age_group'],
        scheduled_for=datetime.strptime(data['scheduled_for'], '%Y-%m-%d %H:%M:%S')
    )
    db.session.add(new_activity)
    db.session.commit()
    return jsonify({"message": "Activity created successfully"}), 201


