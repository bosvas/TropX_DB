import datetime
from dataclasses import dataclass, field
from classes.UserProfile import user_profile
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

# Connect to a PostgreSQL database
# engine = create_engine('postgresql://username:password@host:port/dbname')
# Base = declarative_base()


@dataclass(order=True)
class User():
    # __tablename__ = 'users'
    # user_id = Column(Integer, primary_key=True)
    # name = Column(String)
    # phone = Column(String)
    # email = Column(String)
    # gender = Column(String)
    # birthdate = Column(DateTime)
    # height = Column(Float)
    # weight = Column(Float)
    # sport = Column(String)
    # userProfileId: user_profile = field()
    user_id: int = field()
    name: str = field()
    phone: str = field()
    email: str = field()
    gender: str = field()
    birthdate: datetime = field()
    height: float = field()
    weight: float = field()
    sport: str = field()
    userProfileId: user_profile = field()


# def create_users_table():
#     # create the table
#     Base.metadata.create_all(bind=engine)

