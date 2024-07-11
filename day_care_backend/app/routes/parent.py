#!/usr/bin/python3
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Parent, User, Child, Classroom, Enrollment

parent = Blueprint('parent', __name__)

@parent.route('/', methods=['GET'])
@jwt_required()
def get_all_parents():
    current_user=get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()

    if user.role in ['staff', 'admin']:
        parents = Parent.query.all()
    else:
        return jsonify({"message": "Unauthorized access"}), 403
    return jsonify([parent.to_dict() for parent in parents]), 200

@parent.route('/<int:parent_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def parent_operations(parent_id):
    parent = Parent.query.get_or_404(parent_id)
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()

    if user.role not in ['staff', 'admin'] and parent.user_id != user.user_id:
        return jsonify({"message": "Unauthorized access"}), 403
    
    if request.method == 'GET':
        return jsonify(parent.to_dict()), 200
    elif request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(parent, key, value)
        db.session.commit()
        return jsonify({"message" : "Parent updated successfully"}), 200
    elif request.method == 'DELETE':
        db.session.delete(parent)
        db.session.commit()
        return jsonify({"message": "Parent Deleted successfully"}), 200

@parent.route('/register', methods=['POST'])
@jwt_required()
def register_parent():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role != 'parent':
        return jsonify({"message": "Unauthorized access. Not Parent"}), 401
    
    data = request.get_json()
    new_parent = Parent(
        user_id=user.user_id,
        first_name=data['first_name'],
        last_name=data['last_name'],
        address=data['address'],
        contacts=data['contacts']
    )
    db.session.add(new_parent)
    db.session.commit()
    return jsonify({"message": "Parent registered successfully"}), 201

@parent.route('/child', methods=['POST'])
@jwt_required()
def register_child():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    parent = Parent.query.filter_by(user_id=user.user_id).first()

    if not parent:
        return jsonify({"message": "Parent Not Found "}), 404
    
    data = request.get_json()
    new_child = Child(
        child_name=data['child_name'],
        med_cond=data.get['med_cond'],
        age_group=data['age_group'],
        parent_id=parent.parent_id
    )
    db.session.add(new_child)
    db.session.commit()
    return jsonify({"message": "Child registration successful"}), 201

@parent.route('/enroll', methods=['POST'])
@jwt_required()
def enroll_child():
    data = request.get_json()
    child_id = data.get('child_id')
    if child_id is None:
        return jsonify({"message": "Child ID not provided"}), 400
    class_id = data.get('class_id')
    if class_id is None:
        return jsonify({"message": "Class ID not provided"}), 400
    try:
        child_id = int(child_id)
        class_id = int(class_id)
    except ValueError:
        return jsonify({"message": "Invalid ID format"}), 400

    child = Child.query.get(child_id)
    classroom = Classroom.query.get(class_id)
    
    if not child or not classroom:
        return jsonify({"message": "Child or Classroom not found"}), 404
    
    try:
        new_enrollment = Enrollment(child_id=child.child_id, class_id=classroom.class_id)
        db.session.add(new_enrollment)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "An error occurred while enrolling the child"}), 500
    
    return jsonify({"message": "Child Enrolled successfully"}), 201
