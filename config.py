from flask_sqlalchemy import SQLAlchemy

class Config:
    DEBUG = True
    PORT = 5000
    HOST = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///banco.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


db = SQLAlchemy()