from flask import Flask, render_template, redirect, request
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


load_dotenv()

db_url = os.getenv("DATABASE_URL")
print(db_url)
engine = create_engine(db_url)

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profiles'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    user_name = Column(String)
    user_password = Column(String)
    user_payment_plan = Column(String)
    user_card_details = Column(String)


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    name = Column(String)
    phone = Column(String)
    email = Column(String)
    gender = Column(String)
    birthdate = Column(DateTime)
    height = Column(Float)
    weight = Column(Float)
    sport = Column(String)

    user_profile_id = Column(UUID, ForeignKey('user_profiles.id'))

    medical_information = relationship("MedicalInformation", back_populates="user")

    weights = relationship("Weight", back_populates="user")

    exercise_executions = relationship("ExerciseExecution", back_populates="user")

    def age(self):
        today = datetime.now()
        age = today.year - self.birthdate.year
        if today.month < self.birthdate.month or (today.month == self.birthdate.month and today.day < self.birthdate.day):
            age -= 1
        return age


class Weight(Base):
    __tablename__='weight'
    weight_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    weight = Column(Integer)
    weight_date = Column(DateTime)

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship("User", back_populates="weights")


class MedicalInformation(Base):
    __tablename__ = 'medical_information'
    mi_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    chronic_illness = Column(String)
    orthopedic_status = Column(String)
    current_medication = Column(String)
    balance_sway_standing = Column(Float)
    personal_calibration = Column(String)

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship("User", back_populates="medical_information")

    injuries = relationship("Injury", back_populates="medical_information")


class Injury(Base):
    __tablename__ = 'injuries'
    injury_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    injury_date = Column(Date)
    injury_bodypart = Column(String)
    days_to_recover = Column(Integer)

    medical_information_id = Column(UUID(as_uuid=True), ForeignKey('medical_information.mi_id'))
    medical_information = relationship("MedicalInformation", back_populates="injuries")

    # recover_date = injurie_date + timedelta(days=days_to_recover)
    # is_injured = False
    # if recover_date < datetime.now():
    #     is_injured = True


class ExerciseSpecification(Base):
    __tablename__ = 'exercise_specifications'
    exercise_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    name = Column(String)
    goal = Column(String)
    common_mistakes = Column(String)
    description = Column(String)

    exercise_executions = relationship("ExerciseExecution", back_populates="exercise")


class ExerciseExecution(Base):
    __tablename__ = 'exercise_executions'
    execution_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    execution_date = Column(DateTime)
    number_of_repetitions = Column(Integer)
    number_of_sets = Column(Integer)
    seconds_long = Column(Integer)
    weight_with = Column(Integer)
    correct_rate = Column(Integer)
    is_correct = Column(String)
    where_is_mistake = Column(String)

    exercise_id = Column(UUID(as_uuid=True), ForeignKey('exercise_specifications.exercise_id'))
    exercise = relationship("ExerciseSpecification", back_populates="exercise_executions")

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship("User", back_populates="exercise_executions")


# Create the tables in the database
Base.metadata.create_all(bind=engine)