#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Attendance, User, Child, Classroom
from datetime import datetime 

attendance = Blueprint('attendance', __name__)

@attendance.route('/', methods=['GET'])
@jwt_required()
def get_all_attendance():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role in ['staff', 'admin']:
        attendance_records = Attendance.query.all()
    elif user.role == 'parent':
        children = Child.query.filter_by(parent_id=user.user_id).all()
        attendance_records = []
        for child in children:
            attendance_records.extend(Attendance.query.filter_by(child_id=child.child_id).all())
    else:
        return jsonify({"message": "Unauthorized access"}), 403
    return jsonify([attendance.to_dict() for attendance in attendance_records]), 200

@attendance.route('/<int:attendance_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def attendance_operations(attendance_id):
    attendance_record = Attendance.query.get_or_404(attendance_id)
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role not in ['staff', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 403
    if request.method == 'GET':
        return jsonify(attendance_record.to_dict()), 200
    elif request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(attendance_record, key, value)
        db.session.commit()
        return jsonify({"message": "Attendance updated successfully"}), 200

@attendance.route('/record', methods=['POST'])
@jwt_required()
def record_attendance():
    data = request.get_json()
    new_attendance = Attendance(
        child_id=data['child_id'],
        class_id=data['class_id'],
        present_status=data['present_status'],
        notes=data.get('notes'),
        date=datetime.now().date()
    )
    db.session.add(new_attendance)
    db.session.commit()
    return jsonfiy({"message": "Attendance recorded successfully"}), 201

