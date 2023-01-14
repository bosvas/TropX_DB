from flask import Blueprint, render_template, request
from classes.UserProfile import user_profile_db_implementation


user_profiles_bp = Blueprint('user_profiles_bp', __name__)


@user_profiles_bp.route("/tropx/userprofile/show", methods=['GET'])
def get_all_user_profiles():
    return user_profile_db_implementation.get_all()


@user_profiles_bp.route("/tropx/userprofile/new", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        return user_profile_db_implementation.registration_post()
    return render_template("tropx/userprofile/new.html")


@user_profiles_bp.route('/tropx/userprofile/<id>', methods=['GET', 'POST'])
def get_user_profile(id):
    return user_profile_db_implementation.get_user_profile(id)

@user_profiles_bp.route('/tropx/userprofile/update/<id>', methods=['POST', 'GET'])
def update_user_profile(id):
    if request.method == 'POST':
        return user_profile_db_implementation.update_user_profile_post(id)
    return render_template('tropx/userprofile/update.html')


@user_profiles_bp.route('/tropx/userprofile/delete/<id>', methods=['POST', 'GET'])
def delete_user_profile(id):
    user_profile_db_implementation.delete_user_profile(id)
    return redirect("/tropx/userprofile/show")