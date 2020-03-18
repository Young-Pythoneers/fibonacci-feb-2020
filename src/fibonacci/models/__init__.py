from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()


class Fibonacci(db.Model):
    """ Set fibonacci table structure with two columns.

    First column: Will contain Fibonacci index numbers which are of type int, is set as primary key
    Second column: Will contain Fibonacci numbers of type string.
    """

    __tablename__ = "fibonacci"
    index = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __init__(self, index, value):
        self.index = index
        self.value = value
