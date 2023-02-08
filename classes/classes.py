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

    user_name = Column(String, nullable=False, default="123")
    user_password = Column(String)
    user_payment_plan = Column(String)
    user_card_details = Column(String)

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
    weight_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    weight = Column(Integer)
    weight_date = Column(DateTime)

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
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
    mi_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    chronic_illness = Column(String)
    orthopedic_status = Column(String)
    current_medication = Column(String)
    balance_sway_standing = Column(Float)
    personal_calibration = Column(String)

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
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
    injury_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    injury_date = Column(Date)
    injury_bodypart = Column(String)
    days_to_recover = Column(Integer)

    medical_information_id = Column(UUID(as_uuid=True), ForeignKey('medical_information.mi_id'))
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
    exercise_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    name = Column(String)
    goal = Column(String)
    common_mistakes = Column(String)
    description = Column(String)

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