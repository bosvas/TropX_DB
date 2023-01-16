from flask import Flask, render_template, redirect, request
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
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
    height = Column(Float)
    weight = Column(Float)
    sport = Column(String)
    weights = relationship("Weight", back_populates="user")
    exercise_executions = relationship("ExerciseExecution", back_populates="user")


class Weight(Base):
    __tablename__='weight'
    weight_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    weight = Column(Integer)
    weight_date = Column(DateTime)
    user = relationship("User", back_populates="weights")


class ExerciseSpecification(Base):
    __tablename__ = 'exercise_specifications'
    exercise_id = Column(Integer, primary_key=True)
    name = Column(String)
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
    number_count = Column(Integer)
    weight_with = Column(Integer)
    correct_rate = Column(Integer)
    is_correct = Column(String)


# Create the tables in the database
Base.metadata.create_all(bind=engine)