from flask import Flask, render_template, redirect, Flask, render_template, redirect, request, Blueprint, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from dotenv import load_dotenv
from classes.UserProfile import user_profiles_routes
from classes.PopulationStatistics import population_statistics_routes
from classes.User import user_routes
from classes.ExerciseSpecification import exercise_specification_routes
from classes.ExerciseExecution import exercise_execution_routes
from classes.MedicalInformation import medical_information_routes
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
# from classes.UserProfile.login_routes import login_bp
from classes.classes import UserProfile
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship

# hahaha

load_dotenv()


app = Flask(__name__)
app.register_blueprint(user_profiles_routes.user_profiles_bp)
app.register_blueprint(population_statistics_routes.population_statistics_bp)
app.register_blueprint(user_routes.user_bp)
app.register_blueprint(exercise_specification_routes.exercise_specification_bp)
app.register_blueprint(exercise_execution_routes.exercise_execution_bp)
app.register_blueprint(medical_information_routes.midical_bp)
# app.register_blueprint(login_bp)
#
#


# bootstrap = Bootstrap(app)
# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
#
#
# db_url = os.getenv("DATABASE_URL")
# engine = create_engine(db_url)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# @app.route('/tropx/dashboard')
# @login_required
# def dashboard():
#     return render_template('tropx/userprofile/index.html')
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return UserProfile.query.get(int(user_id))
#
#
# @login_manager.user_loader
# def login(user_name):
#     user_profile = session.query(UserProfile).filter_by(user_name=user_name).first()
#     return user_profile
#
#
# @app.route("/tropx/login", methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         user_name = request.form['user_name']
#         user_password = request.form['user_password']
#         user_profile = UserProfile.query.filter_by(user_name=user_name).first()
#         if user_profile and bcrypt.check_password_hash(user_profile.user_password, user_password):
#             login_user(user_profile)
#             return redirect('/tropx/dashboard')
#         else:
#             flash('Invalid username or password', 'error')
#     return render_template('tropx/userprofile/login.html')
#
#
# @app.route('/tropx/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect('/tropx/login')


@app.route('/')
def index():
    return redirect("tropx/user/show")


if __name__ == '__main__':
    app.run(debug=True, port=5002)
