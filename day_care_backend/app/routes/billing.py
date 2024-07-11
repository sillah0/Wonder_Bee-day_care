#!/usr/bin/python3

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Payment, User

payment = Blueprint('payment', __name__)
@jwt_required()
def get_all_payments():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    
    if user.role in ['staff', 'admin']:
        payments = Payment.query.all()
    else:
        return jsonify({"message": "Unauthorized access"}), 403
    return jsonify([payment.to_dict() for payment in payments]), 200

@payment.route('/<int:payment_id>',methods=['GET'])
@jwt_required()
def get_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    return jsonify(payment.to_dict()), 200

@payment.route('/', methods=['POST'])
@jwt_required()
def create_payment():
    data = request.get_json()
    new_payment = Payment(
        payment_id=data['payment_id'],
        user_id=data['user_id'],
        amount=data['amount'],
        status=data['status'],
        payment_date=data['payment_date']
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify(new_payment.to_dict()), 201

@payment.route('/<int:payment_id>', methods=['PUT'])
@jwt_required()
def update_payment(payment_id):
    data = request.json
    payment = Payment.query.get_or_404(payment_id)
    payment.status = data.get('status', payment.status)
    db.session.commit()
    return jsonify(payment.to_dict()), 200

@payment.route('/<int:payment_id>', methods=['DELETE'])
@jwt_required()
def delete_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify({"message":"payment deleted successfully"}), 200

