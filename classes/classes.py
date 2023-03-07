from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql import func, text
import uuid

from uuid import uuid4


load_dotenv()

db_url = os.getenv("DATABASE_URL")
print(db_url)
engine = create_engine(db_url)

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profiles'
    id = Column(CHAR(36), primary_key=True, default=func.uuid())

    user_name = Column(String(36), nullable=False)
    user_password = Column(String(36))
    user_payment_plan = Column(String(36))
    user_card_details = Column(String(36))

    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "user_password": self.user_password,
            "user_payment_plan": self.user_payment_plan,
            "user_card_details": self.user_card_details,
        }


class User(Base):
    __tablename__ = 'users'
    id = Column(CHAR(36), primary_key=True, default=func.uuid())

    name = Column(String(36))
    phone = Column(String(36))
    email = Column(String(36))
    gender = Column(String(36))
    birthdate = Column(DateTime)
    height = Column(Float)
    weight = Column(Float)
    sport = Column(String(36))

    user_profile_id = Column(CHAR(36), ForeignKey('user_profiles.id'))

    medical_information = relationship("MedicalInformation", back_populates="user")

    weights = relationship("Weight", back_populates="user")

    exercise_executions = relationship("ExerciseExecution", back_populates="user")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "gender": self.gender,
            "birthdate": self.birthdate,
            "height": self.height,
            "weight": self.weight,
            "sport": self.sport,
            "user_profile_id": self.user_profile_id,
            "weights": [weight.to_dict() for weight in self.weights],
            "exercise_executions": [ex_exec.to_dict() for ex_exec in self.exercise_executions],
        }

    def age(self):
        today = datetime.now()
        age = today.year - self.birthdate.year
        if today.month < self.birthdate.month or (today.month == self.birthdate.month and today.day < self.birthdate.day):
            age -= 1
        return age


class Weight(Base):
    __tablename__='weight'
    weight_id = Column(CHAR(36), primary_key=True, default=func.uuid())

    weight = Column(Integer)
    weight_date = Column(DateTime)

    user_id = Column(CHAR(36), ForeignKey('users.id'))
    user = relationship("User", back_populates="weights")

    def to_dict(self):
        return {
            "weight_id": self.weight_id,
            "weight": self.weight,
            "weight_date": self.weight_date,
            "user_id": self.user_id
        }


class MedicalInformation(Base):
    __tablename__ = 'medical_information'
    mi_id = Column(CHAR(36), primary_key=True, default=func.uuid())

    chronic_illness = Column(String(36))
    orthopedic_status = Column(String(36))
    current_medication = Column(String(36))
    balance_sway_standing = Column(Float)
    personal_calibration = Column(String(36))

    user_id = Column(CHAR(36), ForeignKey('users.id'))
    user = relationship("User", back_populates="medical_information")

    injuries = relationship("Injury", back_populates="medical_information")

    def to_dict(self):
        return {
            "mi_id": self.mi_id,
            "chronic_illness": self.chronic_illness,
            "orthopedic_status": self.orthopedic_status,
            "current_medication": self.current_medication,
            "balance_sway_standing": self.balance_sway_standing,
            "personal_calibration": self.personal_calibration,
            "user_id": self.user_id,
            "medical_information": [med_info.to_dict() for med_info in self.medical_information],
            "injuries": [injury.to_dict() for injury in self.injuries]
        }

class Injury(Base):
    __tablename__ = 'injuries'
    injury_id = Column(CHAR(36), primary_key=True, default=func.uuid())

    injury_date = Column(Date)
    injury_bodypart = Column(String(36))
    days_to_recover = Column(Integer)

    medical_information_id = Column(CHAR(36), ForeignKey('medical_information.mi_id'))
    medical_information = relationship("MedicalInformation", back_populates="injuries")

    def to_dict(self):
        return {
            "injury_id": self.injury_id,
            "injury_date": self.injury_date,
            "injury_bodypart": self.injury_bodypart,
            "days_to_recover": self.days_to_recover,
            "medical_information_id": self.medical_information_id
        }


class ExerciseSpecification(Base):
    __tablename__ = 'exercise_specifications'
    exercise_id = Column(CHAR(36), primary_key=True, default=func.uuid())

    name = Column(String(36))
    goal = Column(String(36))
    common_mistakes = Column(String(36))
    description = Column(String(500))

    exercise_executions = relationship("ExerciseExecution", back_populates="exercise")

    def to_dict(self):
        return {
            "exercise_id": self.exercise_id,
            "name": self.name,
            "goal": self.goal,
            "common_mistakes": self.common_mistakes,
            "description": self.description
            # "exercise_executions": [execution.to_dict() for execution in self.exercise_executions]
        }


class ExerciseExecution(Base):
    __tablename__ = 'exercise_executions'
    execution_id = Column(CHAR(36), primary_key=True, default=func.uuid())

    execution_date = Column(DateTime)
    number_of_repetitions = Column(Integer)
    number_of_sets = Column(Integer)
    seconds_long = Column(Integer)
    weight_with = Column(Integer)
    correct_rate = Column(Integer)
    is_correct = Column(String(36))
    where_is_mistake = Column(String(36))

    exercise_id = Column(CHAR(36), ForeignKey('exercise_specifications.exercise_id'))
    exercise = relationship("ExerciseSpecification", back_populates="exercise_executions")

    user_id = Column(CHAR(36), ForeignKey('users.id'))
    user = relationship("User", back_populates="exercise_executions")

    score_to_correct = 80

    def to_dict(self):
        return {
            "execution_id": self.execution_id,
            "execution_date": self.execution_date,
            "number_of_repetitions": self.number_of_repetitions,
            "number_of_sets": self.number_of_sets,
            "seconds_long": self.seconds_long,
            "weight_with": self.weight_with,
            "correct_rate": self.correct_rate,
            "is_correct": self.is_correct,
            "where_is_mistake": self.where_is_mistake,
            "exercise_id": self.exercise_id,
            "user_id": self.user_id
            # "exercise": self.exercise.to_dict() if self.exercise else None,
            # "user": self.user.to_dict() if self.user else None,
        }


# Create the tables in the database
Base.metadata.create_all(bind=engine)