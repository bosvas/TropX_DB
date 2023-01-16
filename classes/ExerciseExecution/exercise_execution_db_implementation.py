import datetime
from flask import Flask, render_template, redirect, request
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from util.weight_plot import weight_histogram_chart
from classes.UserProfile.user_profile_db_implementation import Base

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)


class ExerciseExecution(Base):
    __tablename__ = 'exercise_executions'
    execution_id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey('exercise_specifications.exercise_id'))
    execution_date = Column(DateTime)
    number_count = Column(Integer)
    weight_with = Column(Integer)
    exercise = relationship("ExerciseSpecification", back_populates="exercise_executions")


# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


