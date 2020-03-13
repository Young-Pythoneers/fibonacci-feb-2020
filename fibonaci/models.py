from fibonaci.config import db, ma


class Fibonacci(db.Model):
    """ Set fibonacci table structure with two columns.

    First column: Will contain Fibonacci index numbers which are of type int, is set as primary key
    Second column: Will contain Fibonacci numbers of type string.
    """

    __tablename__ = "fibonacci"
    an_index = db.Column(db.Integer, primary_key=True)
    a_value = db.Column(db.String)


class FibSchema(ma.ModelSchema):
    """ Defines how attributes will be converted to JSON-friendly formats.

    """

    class Meta:
        """ Defines a class named Meta. The ModelSchema class that the PersonSchema
        class inherits from looks for this internal Meta Class and uses it to
        find the SQLAlchemy model Fibonacci and the db.session. Marshmallow finds attributes
        in the Fibonacci class and the type of those attributes to serialize/deserialize them.
        """

        model = Fibonacci
        sqla_session = db.session
