from flask import Flask, render_template, redirect, request
# import os
from dotenv import load_dotenv
from classes.UserProfile import user_profile_db_implementation
from classes.User import user_db_implementation
from classes.PopulationStatistics import population_statictics_db_implementation
from util.weight_plot import weight_histogram_chart

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/tropx/userprofile/new')

@app.route("/tropx/userprofile/show", methods=['GET'])
def get_all_user_profiles():
    return user_profile_db_implementation.get_all()


@app.route("/tropx/userprofile/new", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        return user_profile_db_implementation.registration_post()
    return render_template("tropx/userprofile/new.html")


@app.route('/tropx/userprofile/<id>', methods=['GET', 'POST'])
def get_user_profile(id):
    return user_profile_db_implementation.get_user_profile(id)

@app.route('/tropx/userprofile/update/<id>', methods=['POST', 'GET'])
def update_user_profile(id):
    if request.method == 'POST':
        return user_profile_db_implementation.update_user_profile_post(id)
    return render_template('tropx/userprofile/update.html')


@app.route('/tropx/userprofile/delete/<id>', methods=['POST', 'GET'])
def delete_user_profile(id):
    user_profile_db_implementation.delete_user_profile(id)
    return redirect("/tropx/userprofile/show")


@app.route("/tropx/user/show", methods=['GET'])
def get_all_users():
    users = user_db_implementation.get_all()
    return render_template('tropx/user/index.html', users=users)


@app.route("/tropx/user/new", methods=['GET', 'POST'])
def user_registration():
    if request.method == 'POST':
        return user_db_implementation.registration_post()
    return render_template("tropx/user/new.html")


@app.route('/tropx/user/<id>', methods=['GET', 'POST'])
def get_user(id):
    user, weights = user_db_implementation.get_user(id)
    plot_url = weight_histogram_chart(weights=weights, username=user.name)
    return render_template("tropx/user/show.html", user=user, plot_url=plot_url)


@app.route('/tropx/user/update/<id>', methods=['POST', 'GET'])
def update_user(id):
    if request.method == 'POST':
        return user_db_implementation.update_user_post(id)
    return render_template('tropx/user/update.html')

@app.route('/tropx/user/update/weight/<id>', methods=['POST', 'GET'])
def update_user_weight(id):
    if request.method == 'POST':
        return user_db_implementation.update_user_weight_post(id)
    return render_template('tropx/user/update_weight.html')


@app.route('/tropx/user/delete/<id>', methods=['POST', 'GET'])
def delete_user(id):
    user_db_implementation.delete_user(id)
    return redirect("/tropx/user/show")

@app.route("/tropx/statistic")
def all_population_statistic():
    height, weight = population_statictics_db_implementation.get_population_statistic()
    return render_template('tropx/statistic/index.html', height=height, weight=weight)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
