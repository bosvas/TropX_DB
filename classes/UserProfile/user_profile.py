import datetime
from dataclasses import dataclass, field
from classes.User import user
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@dataclass(order=True)
class UserProfile:
    user_profile_id: int = field()
    # user: user = field()
    user_name: str = field()
    user_password: str = field()
    payment_plan: str = field()
    card_details: str = field()

#
# class UserProfileORM(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)

