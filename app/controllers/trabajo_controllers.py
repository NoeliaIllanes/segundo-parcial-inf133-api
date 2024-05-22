from flask import Blueprint, request, jsonify
from app.models.user import User
from app.utils.database import db
from app.utils.auth import authenticate
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(
        name=data['name'],
        email=data['email'],
        role=data['role']
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Usuario creado"}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = authenticate(data['email'], data['password'])
    if token:
        return jsonify({"access_token": token}), 200
    return jsonify({"message": "Credenciales inválidas"}), 401
