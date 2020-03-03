from config import db, ma

class Fibonacci(db.Model):
    __tablename__ = 'Fibonacci'
    index_value = db.Column(db.Integer, primary_key=True)
    single_value = db.Column(db.Integer)

class FibSchema(ma.ModelSchema):
    class Meta:
        model = Fibonacci
        sqla_session = db.session