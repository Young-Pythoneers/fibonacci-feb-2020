import os
from config import db
from models import Fibonacci

# Data to initialize database with

# Delete database file if it exists currently
if os.path.exists("fibonacci.db"):
    os.remove("fibonacci.db")

# Create the database
db.create_all()

db.session.commit()