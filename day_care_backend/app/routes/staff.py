#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Staff, User, Classroom

staff = Blueprint('staff', __name__)

@staff.route('/', methods=['GET'])
@jwt_required()
def get_all_staff():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role == 'admin':
        staff_members = Staff.query.all()
    else:
        return jsonify({"message": "Unauthorized access"}), 403
    return jsonify([staff.to_dict() for staff in staff_members]), 200

@staff.route('/<int:staff_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def staff_operations(staff_id):
    staff_member = Staff.query.get_or_404(staff_id)
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role != 'admin'and staff_member.user_id != user.user_id:
        return jsonify({"message": "Unauthorized access"}), 403
    if request.method == 'GET':
        return jsonify(staff_member.to_dict()), 200
    elif request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(staff_member, key, value)
        db.session.commit()
        return jsonify({"message": "Staff updated successfully"}), 200
    elif request.method == 'DELETE':
        db.session.delete(staff_member)
        db.session.commit()
        return jsonify({"message": "Staff Deleted"}), 200

@staff.route('/register', methods=['POST'])
@jwt_required()
def register_staff():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role != 'admin':
        return jsonify({"message": "Unauthorized access. Not Admin"}), 401
    
    data = request.get_json()
    new_staff = Staff(
        user_id=user.user_id,
        first_name=data['first_name'],
        last_name=data['last_name'],
        position=data['position'],
        contacts=data['contacts']
    )
    db.session.add(new_staff)
    db.session.commit()
    return jsonify({"message": "Staff registered successfully"}), 201

@staff.route('/assign_classroom', methods=['POST'])
@jwt_required()
def assign_classroom():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role != 'admin':
        return jsonify({"message": "Unauthorized access. Not Admin"}), 401
    
    data = request.get_json()
    staff_member = Staff.query.get_or_404(data['staff_id'])
    classroom = Classroom.query.get_or_404(data['classroom_id'])
    
    staff_member.classroom_id = classroom.classroom_id
    db.session.commit()
    return jsonify({"message": "Classroom assigned successfully"}), 200
