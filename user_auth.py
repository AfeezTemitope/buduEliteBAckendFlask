from flask import request, jsonify
import hashlib
from models import User


def register():
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    email = data.get('email', '').strip()

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    if not User.is_username_unique(username):
        return jsonify({'error': 'Username already taken'}), 400

    validation_result = password_validation(password)
    if validation_result != 'password saved':
        return jsonify({'error': validation_result}), 400

    encrypted_password = encrypt_password(password)

    if User.save(username, encrypted_password, email):
        return jsonify({'message': 'User registered successfully'}), 201
    else:
        return jsonify({'error': 'Registration failed'}), 500


def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'email and password are needed'}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'invalid credentials'}), 401

    if user.password != encrypt_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401
    return jsonify({'message': "successfully loggen in"}), 200


def password_validation(password):
    if len(password) <= 6:
        return 'Password length is too short'
    return 'password saved'


def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
