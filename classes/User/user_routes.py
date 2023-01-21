from flask import Blueprint, render_template, request, redirect
from classes.User import user_db_implementation
from util.weight_plot import weight_histogram_chart

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
    user, weights = user_db_implementation.get_user(id)
    plot_img = weight_histogram_chart(weights=weights, username=user.name)
    return render_template("tropx/user/show.html", user=user, plot_img=plot_img)


@user_bp.route('/tropx/user/update/<id>', methods=['POST', 'GET'])
def update_user(id):
    if request.method == 'POST':
        return user_db_implementation.update_user_post(id)
    return render_template('tropx/user/update.html')

@user_bp.route('/tropx/user/update/weight/<id>', methods=['POST', 'GET'])
def update_user_weight(id):
    if request.method == 'POST':
        return user_db_implementation.update_user_weight_post(id)
    return render_template('tropx/user/update_injurie.html')


@user_bp.route('/tropx/user/delete/<id>', methods=['POST', 'GET'])
def delete_user(id):
    user_db_implementation.delete_user(id)
    return redirect("/tropx/user/show")