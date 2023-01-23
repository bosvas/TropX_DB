from flask import Flask, render_template, redirect, request
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship
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


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    gender = Column(String)
    birthdate = Column(DateTime)
    # age = datetime(year=(datetime.now()-birthdate))
    height = Column(Float)
    weight = Column(Float)
    sport = Column(String)
    user_profile_id = Column(Integer, ForeignKey('user_profiles.id'))
    medical_information = relationship("MedicalInformation", back_populates="user")
    weights = relationship("Weight", back_populates="user")
    exercise_executions = relationship("ExerciseExecution", back_populates="user")


class Weight(Base):
    __tablename__='weight'
    weight_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    weight = Column(Integer)
    weight_date = Column(DateTime)
    user = relationship("User", back_populates="weights")


class MedicalInformation(Base):
    __tablename__ = 'medical_information'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    chronic_illness = Column(String)
    orthopedic_status = Column(String)
    current_medication = Column(String)
    balance_sway_standing = Column(Float)
    personal_calibration = Column(String)
    user = relationship("User", back_populates="medical_information")
    injuries = relationship("Injurie", back_populates="medical_information")


class Injurie(Base):
    __tablename__ = 'injuries'
    injurie_id = Column(Integer, primary_key=True)
    medical_information_id = Column(Integer, ForeignKey('medical_information.id'))
    injurie_date = Column(Date)
    injurie_bodypart = Column(String)
    days_to_recover = Column(Integer)
    medical_information = relationship("MedicalInformation", back_populates="injuries")

    # recover_date = injurie_date + timedelta(days=days_to_recover)
    # is_injured = False
    # if recover_date < datetime.now():
    #     is_injured = True


class ExerciseSpecification(Base):
    __tablename__ = 'exercise_specifications'
    exercise_id = Column(Integer, primary_key=True)
    name = Column(String)
    goal = Column(String)
    common_mistakes = Column(String)
    description = Column(String)
    exercise_executions = relationship("ExerciseExecution", back_populates="exercise")


class ExerciseExecution(Base):
    __tablename__ = 'exercise_executions'
    execution_id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey('exercise_specifications.exercise_id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    exercise = relationship("ExerciseSpecification", back_populates="exercise_executions")
    user = relationship("User", back_populates="exercise_executions")
    execution_date = Column(DateTime)
    number_of_repetitions = Column(Integer)
    number_of_sets = Column(Integer)
    seconds_long = Column(Integer)
    weight_with = Column(Integer)
    correct_rate = Column(Integer)
    is_correct = Column(String)
    where_is_mistake = Column(String)


# Create the tables in the database
Base.metadata.create_all(bind=engine)