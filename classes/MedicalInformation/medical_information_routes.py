from flask import Blueprint, render_template, request, redirect
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


# @midical_bp.route('/tropx/medic/<id>', methods=['GET', 'POST'])
# def get_user(id):
#     user, weights = user_db_implementation.get_user(id)
#     plot_img = weight_histogram_chart(weights=weights, username=user.name)
#     return render_template("tropx/medic/show.html", user=user, plot_img=plot_img)
#
#
# @midical_bp.route('/tropx/medic/delete/<id>', methods=['POST', 'GET'])
# def delete_user(id):
#     user_db_implementation.delete_user(id)
#     return redirect("/tropx/medic/show")