from flask import Blueprint, render_template

task_view_bp = Blueprint('task_view', __name__)

@task_view_bp.route('/tasks')
def task_list():
    return render_template('task_list.html')
