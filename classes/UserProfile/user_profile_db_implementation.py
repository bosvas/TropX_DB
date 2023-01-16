from flask import Flask, render_template, redirect, request
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from classes.classes import UserProfile

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

# Base = declarative_base()
#
# class UserProfile(Base):
#     __tablename__ = 'user_profiles'
#     id = Column(Integer, primary_key=True)
#     user_name = Column(String)
#     user_password = Column(String)
#     user_payment_plan = Column(String)
#     user_card_details = Column(String)
#     # userProfileId: user_profile = field()
#
# # Create the tables in the database
# Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()



def get_all():
    user_profile_list = session.query(UserProfile).all()
    return render_template('tropx/userprofile/index.html', users=user_profile_list)


def registration_post():
    user_name = request.form['user_name']
    user_password = request.form['user_password']
    payment_plan = request.form['payment_plan']
    card_details = request.form['card_details']
    # userProfileId: user_profile = field()
    new_user = UserProfile(user_name=user_name, user_password=user_password, user_payment_plan=payment_plan, user_card_details=card_details)

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
    user_to_update.user_name = user_name
    user_to_update.user_password = user_password
    user_to_update.user_payment_plan = payment_plan
    user_to_update.user_card_details = card_details

    session.commit()

    return redirect("/tropx/userprofile/show")


def delete_user_profile(id):
    user_to_delete = session.query(UserProfile).filter_by(id=id).first()
    session.delete(user_to_delete)
    session.commit()

    return redirect("/tropx/userprofile/show")
