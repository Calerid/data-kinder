import sqlalchemy as sa

engine = 

class DB_Child:
    __tablename__ = 'child'

    name = sa.Column(sa.String, primary_key=True)
    birthdate = sa.Column(sa.DateTime)
    gender = sa.Column(sa.String)
    height = sa.Column(sa.Integer)
    weight = sa.Column(sa.Float)