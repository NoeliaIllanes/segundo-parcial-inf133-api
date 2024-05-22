from flask import Blueprint, request, jsonify
from app.models.task import Task
from app.models.user import User
from app.utils.database import db
from flask_jwt_extended import jwt_required, get_jwt_identity

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

@task_bp.route('/tasks/<int:id>', methods=['GET'])
@jwt_required()
def get_task(id):
    task = Task.query.get(id)
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({"message": "Tarea no encontrada"}), 404

@task_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    task = Task(
        title=data['title'],
        description=data['description'],
        status=data['status'],
        created_at=data['created_at'],
        assigned_to=data['assigned_to']
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

@task_bp.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    data = request.get_json()
    task = Task.query.get(id)
    if task:
        task.status = data['status']
        db.session.commit()
        return jsonify(task.to_dict()), 200
    return jsonify({"message": "Tarea no encontrada"}), 404

@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Tarea eliminada"}), 204
    return jsonify({"message": "Tarea no encontrada"}), 404
