#!/usr/bin/python3

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Enrollment, User, Parent, Child, classroom
from datetime import datetime

enrollment = Blueprint('enrollment', __name__)

@enrollment.route('/', methods=['GET'])
@jwt_required()
def get_all_enrollments():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role in ['staff', 'admin']:
        enrollments = Enrollment.query.all()
    elif user.role == 'parent':
        parent = Parent.query.filter_by(user_id=user.user_id).first()
        children = Child.query.filter_by(parent_id=parent.parent_id).all()
        child_ids = [child.child_id for child in children]
        enrollments = Enrollment.query.filter(Enrollment.child_id.in_(child_ids)).all() 
    else:
        return jsonify({"message": "Unauthorized access"}), 403
    return jsonify([enrollment.to_dict() for enrollment in enrollments]), 200

@enrollment.route('/<int:enrollment_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def enrollment_operations(enrollment_id):
    enrollment = Enrollment.query.get_or_404(enrollment_id)
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role not in ['staff', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 403
    if request.method == 'GET':
        return jsonify(enrollment.to_dict()), 200
    elif request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(enrollment, key, value)
        db.session.commit()
        return jsonify({"message": "Enrollment updated successfully"}), 200
    elif request.method == 'DELETE':
        db.session.delete(enrollment)
        db.session.commit()
        return jsonify({"message": "Enrollment Deleted"}), 200
    
@enrollment.route('/register', methods=['POST'])
@jwt_required()
def create_enrollment():
    data = request.get_json()
    new_enrollment = Enrollment(
        child_id=data['child_id'],
        class_id=data['class_id'],
        date_enrolled=data['date_enrolled']
    )
    db.session.add(new_enrollment)
    db.session.commit()
    return jsonify({"message": "Enrollment created successfully"}), 201
