from flask import Blueprint, render_template, request, redirect, jsonify
from classes.User import user_db_implementation
from util.weight_plot import weight_histogram_chart
from util.injuries_plot import injury_chart
from util.execution_plot import execution_chart

user_bp = Blueprint('user_bp', __name__)


@user_bp.route("/tropx/user/show", methods=['GET'])
def get_all_users():
    users = user_db_implementation.get_all()
    return render_template('tropx/user/index.html', users=users)


@user_bp.route("/tropx/user/new", methods=['GET', 'POST'])
def user_registration():
    if request.method == 'POST':
        return user_db_implementation.registration_post()
    return render_template("tropx/user/new.html")


@user_bp.route('/tropx/user/<id>', methods=['GET', 'POST'])
def get_user(id):
    user, weights, mi, execution_correctness = user_db_implementation.get_user(id)
    plot_img = weight_histogram_chart(weights=weights, username=user.name)
    execution_img = execution_chart(execution_correctness)
    if mi:
        injury_img = injury_chart(injuries=mi.injuries, username=user.name)
    else:
        injury_img = "http://vision4construction.com/uploads/images/safety%20sign.jpg"
    return render_template("tropx/user/show.html", user=user, mi=mi, plot_img=plot_img, injury_img=injury_img, execution_img=execution_img)


@user_bp.route('/tropx/user/update/<id>', methods=['POST', 'GET'])
def update_user(id):
    if request.method == 'POST':
        return user_db_implementation.update_user_post(id)
    return render_template('tropx/user/update.html')


@user_bp.route('/tropx/user/update/weight/<id>', methods=['POST', 'GET'])
def update_user_weight(id):
    if request.method == 'POST':
        return user_db_implementation.update_user_weight_post(id)
    return render_template('tropx/user/update_weight.html')


@user_bp.route('/tropx/user/delete/<id>', methods=['POST', 'GET'])
def delete_user(id):
    user_db_implementation.delete_user(id)
    return redirect("/tropx/user/show")


@user_bp.route('/tropx/user/download')
def download():
    data = user_db_implementation.get_all()
    return jsonify([user_profile.to_dict() for user_profile in data])


@user_bp.route('/tropx/user/json', methods=["POST"])
def upload():
    json_data = request.get_json()
    user_db_implementation.put_json_to_db(json_data)
    return "User_profile created", 201