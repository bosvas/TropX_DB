from flask import Blueprint, render_template, request, redirect, jsonify
from classes.UserProfile import user_profile_db_implementation
from classes.UserProfile.user_profile_db_implementation import session


user_profiles_bp = Blueprint('user_profiles_bp', __name__)


@user_profiles_bp.route("/tropx/userprofile/show", methods=['GET'])
def get_all_user_profiles():
    users = user_profile_db_implementation.get_all()
    return render_template('tropx/userprofile/index.html', users=users)


@user_profiles_bp.route("/tropx/userprofile/new", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        return user_profile_db_implementation.registration_post()
    return render_template("tropx/userprofile/new.html")


# @user_profiles_bp.route("/tropx/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#
#         user_profile = user_profile_db_implementation.login(username)
#         if user_profile and user_profile_db_implementation.verify_password(password, user_profile.user_password):
#             # set the session with the user's ID
#             # session["user_id"] = str(user_profile.id)
#             return user_profile_db_implementation.get_all()
#
#         # otherwise, return an error message
#         return render_template('tropx/userprofile/login.html')
#     return render_template('tropx/userprofile/login.html')


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


@user_profiles_bp.route('/tropx/userprofile/download')
def download():
    data = user_profile_db_implementation.get_all()
    return jsonify([user_profile.to_dict() for user_profile in data])


@user_profiles_bp.route('/tropx/userprofile/json', methods=["POST"])
def upload():
    json_data = request.get_json()
    user_profile_db_implementation.put_json_to_db(json_data)
    return "User_profile created", 201