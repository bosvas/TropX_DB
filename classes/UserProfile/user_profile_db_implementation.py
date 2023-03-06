from flask import Flask, render_template, redirect, request
import os
import json
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from classes.classes import UserProfile
from flask_bcrypt import Bcrypt

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()


def get_all():
    users = session.query(UserProfile).all()
    return users


def registration_post():
    user_name = request.form['user_name']
    payment_plan = request.form['payment_plan']
    card_details = request.form['card_details']

    user_password = request.form['user_password']
    hashed_password = Bcrypt().generate_password_hash(user_password).decode('utf-8')
    print(hashed_password)

    new_user = UserProfile(user_name=user_name, user_password=hashed_password, user_payment_plan=payment_plan, user_card_details=card_details)

    session.add(new_user)
    session.commit()

    return redirect("/tropx/userprofile/show")


def get_user_profile(id):
    user_profile = session.query(UserProfile).filter_by(id=id).first()

    return render_template("tropx/userprofile/show.html", user=user_profile)


def update_user_profile_post(id):
    user_name = request.form['user_name']
    user_password = request.form['user_password']
    payment_plan = request.form['payment_plan']
    card_details = request.form['card_details']

    user_to_update = session.query(UserProfile).filter_by(id=id).first()
    hashed_password = Bcrypt().generate_password_hash(user_password).decode('utf-8')
    print(verify_password(user_password, hashed_password))
    user_to_update.user_name = user_name
    user_to_update.user_password = hashed_password
    user_to_update.user_payment_plan = payment_plan
    user_to_update.user_card_details = card_details

    session.commit()

    return redirect("/tropx/userprofile/show")


def delete_user_profile(id):
    user_to_delete = session.query(UserProfile).filter_by(id=id).first()
    session.delete(user_to_delete)
    session.commit()

    return redirect("/tropx/userprofile/show")


def put_json_to_db(data):

    user_password = data["user_password"]
    hashed_password = Bcrypt().generate_password_hash(user_password).decode('utf-8')

    new_user = UserProfile(
        user_name=data["user_name"],
        user_password=hashed_password,
        user_payment_plan=data["user_payment_plan"],
        user_card_details=data["user_card_details"]
    )

    session.add(new_user)
    session.commit()


def verify_password(password, hashed_password):
    return Bcrypt().check_password_hash(hashed_password, password)