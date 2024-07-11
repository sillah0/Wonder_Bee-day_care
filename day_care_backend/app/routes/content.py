#!/usr/bin/python3

from flask import Blueprint, jsonify
from utils.decorator import role_required

content = Blueprint('content', __name__)

@content.route('/admin', methods=['GET'])
@role_required(['admin'])
def admin_route():
    return jsonify({"message": "Admin access granted"}), 200

@content.route('/staff', methods=['GET'])
@role_required(['admin', 'staff'])
def staff_route():
    return jsonify({"message": "Staff access granted"}), 200

@content.route('/parent', methods=['GET'])
@role_required(['admin', 'parent'])
def parent_route():
    return jsonify({"message": "Parent access granted"}), 200
