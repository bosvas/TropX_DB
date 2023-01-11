from flask import Flask, render_template, redirect, request
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

db_url = os.getenv("DATABASE_URL")
print(db_url)
engine = create_engine(db_url)

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profiles'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_password = Column(String)
    user_payment_plan = Column(String)
    user_card_details = Column(String)
    # userProfileId: user_profile = field()

# Create the tables in the database
Base.metadata.create_all(bind=engine)

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




#
# from flask import Flask, render_template, redirect, request
# import os
# import psycopg2
# from dotenv import load_dotenv
# from classes.UserProfile.user_profile import UserProfile
#
# load_dotenv()
#
# url_db = os.getenv("DATABASE_URL")
# connection = psycopg2.connect(url_db)
#
# CREATE_USER_PROFILE_TABLE = """
# CREATE TABLE IF NOT EXISTS user_profiles(
#                        id SERIAL PRIMARY KEY,
#                        user_name VARCHAR(25) NOT NULL,
#                        user_password VARCHAR(20) NOT NULL,
#                        user_payment_plan VARCHAR(20),
#                        user_card_details VARCHAR(20)
# );
# """
# INSERT_USER_PROFILE = """INSERT INTO user_profiles (user_name, user_password, user_payment_plan, user_card_details)
#                                 VALUES (%s, %s, %s, %s);"""
# GET_ONE_USER_PROFILE_BY_ID = "SELECT * FROM user_profiles WHERE id = %s"
# SELECT_ALL_USER_PROFILES = "SELECT * FROM user_profiles"
# UPDATE_ONE = """UPDATE user_profiles SET user_name = %s, user_password = %s,
#                 user_payment_plan = %s, user_card_details = %s WHERE id = %s"""
# DELETE_ONE = "DELETE FROM user_profiles WHERE id = %s"
# # GET_PERSON_ID = "SELECT id FROM user_profiles WHERE user_name = %s"
#
# def get_all():
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(CREATE_USER_PROFILE_TABLE)
#             cursor.execute(SELECT_ALL_USER_PROFILES)
#             user_profile_tuples = cursor.fetchall()
#             user_profile_list = [UserProfile(*user_profile) for user_profile in user_profile_tuples]
#
#     return render_template('tropx/userprofile/index.html', users=user_profile_list)
#
#
# def registration_post():
#     user_name = request.form['user_name']
#     user_password = request.form['user_password']
#     payment_plan = request.form['payment_plan']
#     card_details = request.form['card_details']
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(CREATE_USER_PROFILE_TABLE)
#             cursor.execute(INSERT_USER_PROFILE, (user_name, user_password, payment_plan, card_details))
#     return redirect("/tropx/userprofile/show")
#
# # def registration_get():
# #     if request.method == 'POST':
# #
# #     return render_template("tropx/userprofile/new.html")
#
#
# def get_user_profile(id):
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(GET_ONE_USER_PROFILE_BY_ID, (id,))
#             user_profile_data = cursor.fetchall()
#             user_profile = UserProfile(user_profile_data[0][0], user_profile_data[0][1],
#                                        user_profile_data[0][2], user_profile_data[0][3],
#                                        user_profile_data[0][4])
#
#     return render_template("tropx/userprofile/show.html", user=user_profile)
#
#
# def update_user_profile_post(id):
#     user_name = request.form['user_name']
#     user_password = request.form['user_password']
#     payment_plan = request.form['payment_plan']
#     card_details = request.form['card_details']
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(UPDATE_ONE, (user_name, user_password, payment_plan, card_details, id))
#     return redirect("/tropx/userprofile/show")
#
#
# def delete_user_profile(id):
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(DELETE_ONE, (id,))
#
#     return redirect("/tropx/userprofile/show")