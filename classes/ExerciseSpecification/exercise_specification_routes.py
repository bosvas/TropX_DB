from flask import Blueprint, render_template, request, redirect, jsonify
from classes.ExerciseSpecification import exercise_specification_db_implementation

exercise_specification_bp = Blueprint('exercise_specification_bp', __name__)


@exercise_specification_bp.route("/tropx/exercise/show", methods=['GET'])
def get_all_exercises():
    exercises = exercise_specification_db_implementation.get_all()
    return render_template('tropx/exercise/index.html', exercises=exercises)


@exercise_specification_bp.route("/tropx/exercise/new", methods=['GET', 'POST'])
def new_exercise():
    if request.method == 'POST':
        return exercise_specification_db_implementation.new_exercise()
    return render_template("tropx/exercise/new.html")


@exercise_specification_bp.route('/tropx/exercise/<id>', methods=['GET', 'POST'])
def get_exercise(id):
    exercise = exercise_specification_db_implementation.get_exercise(id)
    return render_template("tropx/exercise/show.html", exercise=exercise)


@exercise_specification_bp.route('/tropx/exercise/update/<id>', methods=['POST', 'GET'])
def update_exercise(id):
    if request.method == 'POST':
        return exercise_specification_db_implementation.update_exercise_post(id)
    return render_template('tropx/exercise/update.html')


@exercise_specification_bp.route('/tropx/exercise/delete/<id>', methods=['POST', 'GET'])
def delete_exercise(id):
    exercise_specification_db_implementation.delete_exercise(id)
    return redirect("/tropx/exercise/show")


@exercise_specification_bp.route('/tropx/exercise/download')
def download():
    data = exercise_specification_db_implementation.get_all()
    return jsonify([specification.to_dict() for specification in data])


@exercise_specification_bp.route('/tropx/exercise/json', methods=["POST"])
def upload():
    json_data = request.get_json()
    exercise_specification_db_implementation.put_json_to_db(json_data)
    return "exercise_specification created", 201