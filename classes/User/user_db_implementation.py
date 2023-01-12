import datetime

from flask import Flask, render_template, redirect, request
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from util.weight_plot import weight_histogram_chart


load_dotenv()

db_url = os.getenv("DATABASE_URL")
print(db_url)
engine = create_engine(db_url)

Base = declarative_base()

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
    # userProfileId: user_profile = field()


class Weight(Base):
    __tablename__='weight'
    weight_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    weight = Column(Integer)
    weight_date = Column(DateTime)
    user = relationship("User", back_populates="weights")


# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


def get_all():
    users = session.query(User).all()
    return users


def registration_post():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    gender = request.form['gender']
    birthdate = request.form['birthdate']
    height = request.form['height']
    weight = request.form['weight']
    sport = request.form['sport']
    # userProfileId: user_profile = field()
    new_user = User(name=name, phone=phone, email=email, gender=gender, birthdate=birthdate, height=height, weight=weight, sport=sport)
    new_weight = Weight(user_id=new_user.id, weight=weight, weight_date=datetime.datetime.now())
    session.add(new_weight)

    session.add(new_user)
    session.commit()

    return redirect("/tropx/user/show")


def get_user(id):
    user = session.query(User).filter_by(id=id).first()
    weights = session.query(Weight).filter_by(user_id=id)

    return (user, weights)


def update_user_post(id):
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    gender = request.form['gender']
    birthdate = request.form['birthdate']
    height = request.form['height']
    weight = request.form['weight']
    sport = request.form['sport']

    user_to_update = session.query(User).filter_by(id=id).first()
    user_to_update.name = name
    user_to_update.phone = phone
    user_to_update.email = email
    user_to_update.gender = gender
    user_to_update.birthdate = birthdate
    user_to_update.height = height
    user_to_update.weight = weight
    user_to_update.sport = sport

    new_weight = Weight(user_id=user_to_update.id, weight=weight, weight_date=datetime.datetime.now())
    session.add(new_weight)

    session.commit()

    return redirect("/tropx/user/show")


def update_user_weight_post(id):
    weight = request.form['weight']
    user_to_update = session.query(User).filter_by(id=id).first()
    user_to_update.weight = weight
    new_weight = Weight(user_id=user_to_update.id, weight=weight, weight_date=datetime.datetime.now())
    session.add(new_weight)

    session.commit()

    return redirect(f"/tropx/user/{user_to_update.id}")

def delete_user(id):
    user_to_delete = session.query(User).filter_by(id=id).first()
    session.delete(user_to_delete)
    session.commit()

    return redirect("/tropx/user/show")


