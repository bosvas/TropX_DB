import datetime
from flask import Flask, render_template, redirect, request
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from util.weight_plot import weight_histogram_chart
from classes.User import user_db_implementation
from classes.ExerciseSpecification import exercise_specification_db_implementation
from classes.classes import ExerciseExecution
from classes.classes import User

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)


Session = sessionmaker(bind=engine)
session = Session()



def get_all_executions():
    exercise_executions = session.query(ExerciseExecution).all()

    return exercise_executions


def new_exercise_execution():
    execution_date = request.form['execution_date']
    number_of_repetitions = request.form['number_of_repetitions']
    number_of_sets = request.form['number_of_sets']
    seconds_long = request.form['seconds_long']
    weight_with = request.form['weight_with']
    correct_rate = request.form['correct_rate']
    is_correct = request.form['is_correct']
    exercise_id = request.form['exercise_id']
    user_name = request.form['user_name']
    where_is_mistake = request.form['where_is_mistake']

    user = session.query(User).filter_by(name=user_name).first()

    new_exercise = ExerciseExecution(user_id=user.id, exercise_id=exercise_id, execution_date=execution_date,
                                     number_of_repetitions=number_of_repetitions, number_of_sets=number_of_sets,
                                     weight_with=weight_with, correct_rate=correct_rate, seconds_long=seconds_long,
                                     is_correct=is_correct, where_is_mistake=where_is_mistake)

    session.add(new_exercise)
    session.commit()

    return redirect("/tropx/exercise/show")


def get_exercise_execution(id):
    exercise_execution = session.query(ExerciseExecution).filter_by(execution_id=id).first()
    return exercise_execution

def update_exercise_execution_post(id):
    execution_date = request.form['execution_date']
    number_of_repetitions = request.form['number_of_repetitions']
    number_of_sets = request.form['number_of_sets']
    seconds_long = request.form['seconds_long']
    weight_with = request.form['weight_with']
    correct_rate = request.form['correct_rate']
    is_correct = request.form['is_correct']
    exercise_id = request.form['exercise_id']
    user_id = request.form['user_id']
    where_is_mistake = request.form['where_is_mistake']

    exercise_to_update = session.query(ExerciseExecution).filter_by(execution_id=id).first()

    exercise_to_update.execution_date = execution_date
    exercise_to_update.number_of_repetitions = number_of_repetitions
    exercise_to_update.number_of_sets = number_of_sets
    exercise_to_update.seconds_long = seconds_long
    exercise_to_update.weight_with = weight_with
    exercise_to_update.correct_rate = correct_rate
    exercise_to_update.is_correct = is_correct
    exercise_to_update.exercise_id = exercise_id
    exercise_to_update.user_id = user_id
    exercise_to_update.where_is_mistake = where_is_mistake

    session.commit()

    return redirect("/tropx/exercise/show")


def delete_exercise_execution(id):
    exercise_to_delete = session.query(ExerciseExecution).filter_by(execution_id=id).first()
    session.delete(exercise_to_delete)
    session.commit()

    return redirect("/tropx/exercise/show")


def put_json_to_db(data):

    execution_date = data['execution_date']
    number_of_repetitions = data['number_of_repetitions']
    number_of_sets = data['number_of_sets']
    seconds_long = data['seconds_long']
    weight_with = data['weight_with']
    correct_rate = data['correct_rate']
    is_correct = data['is_correct']
    exercise_id = data['exercise_id']
    user_id = data['user_id']
    where_is_mistake = data['where_is_mistake']

    new_exercise = ExerciseExecution(user_id=user_id, exercise_id=exercise_id, execution_date=execution_date,
                                     number_of_repetitions=number_of_repetitions, number_of_sets=number_of_sets,
                                     weight_with=weight_with, correct_rate=correct_rate, seconds_long=seconds_long,
                                     is_correct=is_correct, where_is_mistake=where_is_mistake)

    session.add(new_exercise)
    session.commit()



# TODO механизм подставления айди упражнения кажется надо переделать, и вообще возможно переделать чтобы там было имя а не айди??
