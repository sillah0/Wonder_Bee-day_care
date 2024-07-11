#!/usr/bin/python3

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Classroom, User, Staff

classroom = Blueprint('classroom', __name__)

@classroom.route('/', methods=['GET'])
@jwt_required()
def get_all_classrooms():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role in ['staff', 'admin']:
        classrooms = Classroom.query.all()
    else:
        return jsonify({"message": "Unauthorized access"}), 403
    return jsonify([classroom.to_dict() for classroom in classrooms]), 200

@classroom.route('/<int:classroom_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def classroom_operations(class_id):
    classroom = Classroom.query.get_or_404(class_id)
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role not in ['staff', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 403
    if request.method == 'GET':
        return jsonify(classroom.to_dict()), 200
    elif request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(classroom, key, value)
        db.session.commit()
        return jsonify({"message": "Classroom updated successfully"}), 200
    elif request.method == 'DELETE':
        db.session.delete(classroom)
        db.session.commit()
        return jsonify({"message": "Classroom Deleted"}), 200

@classroom.route('/create', methods=['POST'])
@jwt_required()
def create_classrooms():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role != 'admin':
        return jsonify({"message": "Unauthorized access. Not Admin"}), 401
    data = request.get_json()
    new_classroom = Classroom(
        teacher_id=data['teacher_id'],
        class_name=data['class_name'],
    )
    db.session.add(new_classroom)
    db.session.commit()
    return jsonify({"message": "Classroom created successfully"}), 201

