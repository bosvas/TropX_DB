from flask import Blueprint, render_template, request, redirect, jsonify
from classes.User import user_db_implementation
from util.weight_plot import weight_histogram_chart
from classes.MedicalInformation import medical_information_db_implementation

midical_bp = Blueprint('medic_bp', __name__)


@midical_bp.route("/tropx/medic/show", methods=['GET'])
def get_all_medical_information():
    medical_informations = medical_information_db_implementation.get_all()
    return render_template('tropx/medic/index.html', medical_informations=medical_informations)


@midical_bp.route("/tropx/user/medic/new/<id>", methods=['GET', 'POST'])
def medic_registration(id):
    if request.method == 'POST':
        return medical_information_db_implementation.add_user_medical_information(id)
    return render_template("tropx/medic/new.html")


@midical_bp.route('/tropx/user/medic/update/<id>', methods=['POST', 'GET'])
def update_medical(id):
    if request.method == 'POST':
        return medical_information_db_implementation.update_medical_information_post(id)
    return render_template('tropx/medic/update.html')


@midical_bp.route('/tropx/user/update/injury/<id>', methods=['POST', 'GET'])
def update_medic_injury(id):
    if request.method == 'POST':
        return medical_information_db_implementation.update_medical_information_injury_post(id)
    return render_template('tropx/medic/update_injury.html')

# @midical_bp.route('/tropx/medical/download')
# def download():
#     data = medical_information_db_implementation.get_all()
#     return jsonify([user_profile.to_dict() for user_profile in data])
#
#
# @midical_bp.route('/tropx/medical/json', methods=["POST"])
# def upload():
#     json_data = request.get_json()
#     medical_information_db_implementation.put_json_to_db(json_data)
#     return "User_profile created", 201