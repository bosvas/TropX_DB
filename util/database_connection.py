# from flask import Flask
# from sqlalchemy import create_engine
#
# class DatabaseConnection:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#            cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         self.engine = create_engine('postgresql://username:password@host:port/dbname')
#
#
# app = Flask(__name__)
# db = DatabaseConnection()