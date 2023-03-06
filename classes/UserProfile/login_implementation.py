# import login as login
# from flask import Flask, render_template, redirect, request, Blueprint, flash
# from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
# from classes.classes import UserProfile
# from bcrypt import hashpw, gensalt, checkpw
# from flask_bcrypt import Bcrypt
# from app import login_manager, bcrypt
# from login_routes import login_bp
#
#
# # login_bp = Blueprint('login_bp', __name__)
#
# load_dotenv()
#
# db_url = os.getenv("DATABASE_URL")
# engine = create_engine(db_url)
#
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# login_manager.login_view = 'login'
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return UserProfile.query.get(int(user_id))
#
#
# @login_bp.route("/tropx/login", methods=['GET', 'POST'])
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
# @login_manager.user_loader
# def login(user_name):
#     user_profile = session.query(UserProfile).filter_by(user_name=user_name).first()
#
#     return user_profile
#
#
# @login_bp.route('/tropx/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect('/tropx/login')