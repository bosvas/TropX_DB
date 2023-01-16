import datetime
from flask import Flask, render_template, redirect, request
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from util.weight_plot import weight_histogram_chart
# from classes.UserProfile.user_profile_db_implementation import Base
from classes.User import user_db_implementation
from classes.ExerciseSpecification import exercise_specification_db_implementation
from classes.classes import ExerciseExecution

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

# Base = declarative_base()

# class ExerciseExecution(Base):
#     __tablename__ = 'exercise_executions'
#     execution_id = Column(Integer, primary_key=True)
#     exercise_id = Column(Integer, ForeignKey('exercise_specifications.exercise_id'))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     exercise = relationship("ExerciseSpecification", back_populates="exercise_executions")
#     user = relationship("User", back_populates="exercise_executions")
#     execution_date = Column(DateTime)
#     number_count = Column(Integer)
#     weight_with = Column(Integer)
#     correct_rate = Column(Integer)
#     is_correct = Column(String)


# Create the tables in the database
# Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()



def get_all_executions():
    exercise_executions = session.query(ExerciseExecution).all()
    # users = []
    # exercise = []
    # for execution in exercise_executions:
    #


    return exercise_executions


def new_exercise_execution():
    execution_date = request.form['execution_date']
    number_count = request.form['number_count']
    weight_with = request.form['weight_with']
    correct_rate = request.form['correct_rate']
    is_correct = request.form['is_correct']
    exercise_id = request.form['exercise_id']
    user_id = request.form['user_id']

    new_exercise = ExerciseExecution(user_id=user_id, exercise_id=exercise_id, execution_date=execution_date, number_count=number_count, weight_with=weight_with, correct_rate=correct_rate, is_correct=is_correct)

    session.add(new_exercise)
    session.commit()

    return redirect("/tropx/exercise/show")


def get_exercise_execution(id):
    exercise_execution = session.query(ExerciseExecution).filter_by(execution_id=id).first()
    user = user_db_implementation.get_user(exercise_execution.user_id)
    exercise = exercise_specification_db_implementation.get_exercise(exercise_execution.exercise_id)
    return (exercise_execution, user, exercise)


def update_exercise_execution_post(id):
    execution_date = request.form['execution_date']
    number_count = request.form['number_count']
    weight_with = request.form['weight_with']
    correct_rate = request.form['correct_rate']
    is_correct = request.form['is_correct']
    exercise_id = request.form['exercise_id']

    exercise_to_update = session.query(ExerciseExecution).filter_by(execution_id=id).first()

    exercise_to_update.execution_date = execution_date
    exercise_to_update.number_count = number_count
    exercise_to_update.weight_with = weight_with
    exercise_to_update.correct_rate = correct_rate
    exercise_to_update.is_correct = is_correct
    exercise_to_update.exercise_id = exercise_id

    session.commit()

    return redirect("/tropx/exercise/show")


def delete_exercise_execution(id):
    exercise_to_delete = session.query(ExerciseExecution).filter_by(execution_id=id).first()
    session.delete(exercise_to_delete)
    session.commit()

    return redirect("/tropx/exercise/show")

