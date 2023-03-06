import login as login
from flask import Flask, render_template, redirect, request, Blueprint, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from classes.classes import UserProfile
from bcrypt import hashpw, gensalt, checkpw
from flask_bcrypt import Bcrypt
from app import app


load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)


Session = sessionmaker(bind=engine)
session = Session()

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

login_bp = Blueprint('login_bp', __name__)


@login_manager.user_loader
def login(user_name):
    user_profile = session.query(UserProfile).filter_by(user_name=user_name).first()

    return user_profile


@login_bp.route("/tropx/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserProfile.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect('/tropx/dashboard')
        else:
            flash('Invalid username or password', 'error')
    return render_template('tropx/userprofile/login.html')


@login_bp.route('/tropx/dashboard')
@login_required
def dashboard():
    return render_template('tropx/userprofile/index.html')


@login_bp.route('/tropx/logout')
@login_required
def logout():
    logout_user()
    return redirect('/tropx/login')