from fibonaci.config import db, ma

class Fibonacci(db.Model):
    __tablename__ = 'fibonacci'
    an_index = db.Column(db.Integer, primary_key=True)
    a_value = db.Column(db.String)

class FibSchema(ma.ModelSchema):
    class Meta:
        model = Fibonacci
        sqla_session = db.session