#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user import User
from models import db
from marshmallow import ValidationError, Schema, fields, validate

auth = Blueprint('auth', __name__)

class UserSchema(Schema):
    first_name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    last_name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8))
    role = fields.Str(required=True, validate=validate.OneOf(['parent', 'staff', 'admin']))

@auth.route('register', methods=['POST'])
def register():
    schema = UserSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email already exists"}), 400
    
    hashed_password = generate_password_hash(data['password'])
    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=hashed_password,
        role=data['role']
    )

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "An error occurred while registering the user"}), 500
    return jsonify({"message": "User registered successfully"}), 201

@auth.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity={"email": email, "role": user.role})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401

@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify({"message": "logout successful"}), 200
