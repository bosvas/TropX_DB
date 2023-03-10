from flask import Blueprint, render_template, request, redirect, jsonify
from classes.ExerciseExecution import exercise_execution_db_implementation
from classes.User import user_db_implementation

exercise_execution_bp = Blueprint('exercise_execution_bp', __name__)


@exercise_execution_bp.route("/tropx/execution/show", methods=['GET'])
def get_all_exercises():
    exercise_executions = exercise_execution_db_implementation.get_all_executions()
    return render_template('tropx/execution/index.html', exercise_executions=exercise_executions)


@exercise_execution_bp.route("/tropx/execution/new", methods=['GET', 'POST'])
def new_exercise():
    if request.method == 'POST':
        return exercise_execution_db_implementation.new_exercise_execution()
    users = user_db_implementation.get_all()
    return render_template("tropx/execution/new.html", users=users)


@exercise_execution_bp.route('/tropx/execution/<id>', methods=['GET', 'POST'])
def get_exercise(id):
    execution = exercise_execution_db_implementation.get_exercise_execution(id)
    return render_template("tropx/execution/show.html", execution=execution)


@exercise_execution_bp.route('/tropx/execution/update/<id>', methods=['POST', 'GET'])
def update_exercise(id):
    if request.method == 'POST':
        return exercise_execution_db_implementation.update_exercise_execution_post(id)
    return render_template('tropx/execution/update.html')


@exercise_execution_bp.route('/tropx/execution/delete/<id>', methods=['POST', 'GET'])
def delete_exercise(id):
    exercise_execution_db_implementation.delete_exercise_execution(id)
    return redirect("/tropx/execution/show")


@exercise_execution_bp.route('/tropx/execution/download')
def download():
    data = exercise_execution_db_implementation.get_all_executions()
    return jsonify([user_profile.to_dict() for user_profile in data])


@exercise_execution_bp.route('/tropx/execution/json', methods=["POST"])
def upload():
    json_data = request.get_json()
    exercise_execution_db_implementation.put_json_to_db(json_data)
    return "Exercise execution created", 201