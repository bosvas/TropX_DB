import datetime
from flask import Flask, render_template, redirect, request
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
# from classes.UserProfile.user_profile_db_implementation import Base
from classes.classes import User, Weight, MedicalInformation, Injury


load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)


Session = sessionmaker(bind=engine)
session = Session()


def get_all():
    medical_informations = session.query(MedicalInformation).all()
    return medical_informations


def add_user_medical_information(id):
    chronic_illness = request.form['chronic_illness']
    orthopedic_status = request.form['orthopedic_status']
    current_medication = request.form['current_medication']
    balance_sway_standing = request.form['balance_sway_standing']
    personal_calibration = request.form['personal_calibration']

    new_medical_information = MedicalInformation\
        (user_id=id, chronic_illness=chronic_illness, orthopedic_status=orthopedic_status,
         current_medication=current_medication, balance_sway_standing=balance_sway_standing,
         personal_calibration=personal_calibration)
    session.add(new_medical_information)

    session.commit()

    return redirect(f"/tropx/user/{id}")


def update_medical_information_post(id):
    chronic_illness = request.form['chronic_illness']
    orthopedic_status = request.form['orthopedic_status']
    current_medication = request.form['current_medication']
    balance_sway_standing = request.form['balance_sway_standing']
    personal_calibration = request.form['personal_calibration']

    # injurie_date = request.form['injurie_date']
    # injurie_bodypart = request.form['injurie_bodypart']
    # days_to_recover = request.form['days_to_recover']

    user_to_update = session.query(User).filter_by(id=id).first()
    medical_information_to_update = session.query(MedicalInformation).filter_by(user_id=user_to_update.id).first()

    medical_information_to_update.chronic_illness = chronic_illness
    medical_information_to_update.orthopedic_status = orthopedic_status
    medical_information_to_update.current_medication = current_medication
    medical_information_to_update.balance_sway_standing = balance_sway_standing
    medical_information_to_update.personal_calibration = personal_calibration

    # new_injurie = Injurie(medical_information_id=medical_information_to_update.id,
    #                           injurie_date=injurie_date, injurie_bodypart=injurie_bodypart,
    #                           days_to_recover=days_to_recover)
    # session.add(new_injurie)

    session.commit()

    return redirect(f"/tropx/user/{id}")


def update_medical_information_injury_post(id):
    injury_date = request.form['injury_date']
    injury_bodypart = request.form['injury_bodypart']
    days_to_recover = request.form['days_to_recover']

    user_to_update = session.query(User).filter_by(id=id).first()
    user_id = user_to_update.id
    medical_information_to_update = session.query(MedicalInformation).filter_by(user_id=user_id).first()
    mi_id = medical_information_to_update.mi_id
    new_injury = Injury(medical_information_id=mi_id, injury_date=injury_date, injury_bodypart=injury_bodypart, days_to_recover=days_to_recover)
    # new_injury.medical_information_id = mi.id

    session.add(new_injury)

    session.commit()

    return redirect(f"/tropx/user/{user_to_update.id}")


# def put_json_to_db(data):
#     chronic_illness = data['chronic_illness']
#     orthopedic_status = data['orthopedic_status']
#     current_medication = data['current_medication']
#     balance_sway_standing = data['balance_sway_standing']
#     personal_calibration = data['personal_calibration']
#
#     new_medical_information = MedicalInformation\
#         (user_id=id, chronic_illness=chronic_illness, orthopedic_status=orthopedic_status,
#          current_medication=current_medication, balance_sway_standing=balance_sway_standing,
#          personal_calibration=personal_calibration)
#     session.add(new_medical_information)
#
#     session.commit()
#
#     return redirect(f"/tropx/user/{id}")


