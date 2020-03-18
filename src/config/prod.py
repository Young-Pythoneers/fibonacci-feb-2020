import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(basedir, "fibonacci_database.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
