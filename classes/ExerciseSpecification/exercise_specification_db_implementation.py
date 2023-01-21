import datetime
from flask import Flask, render_template, redirect, request
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from util.weight_plot import weight_histogram_chart
# from classes.UserProfile.user_profile_db_implementation import Base
from classes.ExerciseExecution.exercise_execution_db_implementation import ExerciseExecution
from classes.classes import ExerciseSpecification

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)


# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


def get_all():
    exercises = session.query(ExerciseSpecification).all()
    return exercises


def new_exercise():
    name = request.form['name']
    description = request.form['description']
    goal = request.form['goal']
    common_mistakes = request.form['common_mistakes']

    new_exercise = ExerciseSpecification(name=name, description=description, goal=goal, common_mistakes=common_mistakes)

    session.add(new_exercise)
    session.commit()

    return redirect("/tropx/exercise/show")


def get_exercise(id):
    exercise = session.query(ExerciseSpecification).filter_by(exercise_id=id).first()
    # executions = session.query(ExerciseExecution).filter_by(exercise_id=id)

    return exercise


def update_exercise_post(id):
    name = request.form['name']
    description = request.form['description']
    goal = request.form['goal']
    common_mistakes = request.form['common_mistakes']

    exercise_to_update = session.query(ExerciseSpecification).filter_by(exercise_id=id).first()
    exercise_to_update.name = name
    exercise_to_update.description = description
    exercise_to_update.goal = goal
    exercise_to_update.common_mistakes = common_mistakes

    session.commit()

    return redirect("/tropx/exercise/show")


def delete_exercise(id):
    exercise_to_delete = session.query(ExerciseSpecification).filter_by(exercise_id=id).first()
    session.delete(exercise_to_delete)
    session.commit()

    return redirect("/tropx/exercise/show")
