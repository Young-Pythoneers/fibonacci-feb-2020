from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()


class Fibonacci(db.Model):
    """ Set fibonacci table structure with two columns.

    First column: Will contain Fibonacci index numbers which are of type int, is set as primary key
    Second column: Will contain Fibonacci numbers of type string.
    """

    __tablename__ = "fibonacci"
    an_index = db.Column(db.Integer, primary_key=True)
    a_value = db.Column(db.String)

    def __init__(self, an_index, a_value):
        self.an_index = an_index
        self.a_value = a_value
