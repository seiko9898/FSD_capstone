import os
from sqlalchemy import Column, String, Integer, create_engine, Date, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_name = "casting"
#database_path = "postgresql://postgres:abcde@localhost:5432/casting"
database_path = "postgres://ucejfccbbzvkjo:0968201613aaae144435948fa46f5fa4264c5bb5b708aed78c114320da58026d@ec2-52-7-39-178.compute-1.amazonaws.com:5432/df5al5nci0lgp8"
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    #db.drop_all()
    #db.create_all()
    migrate = Migrate(app, db)

class Movie(db.Model):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }


class Actor(db.Model):
    __tablename__ = 'actor'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age':self.age,
            'gender': self.gender
        }


class Actor_Movie(db.Model):
    __tablename__ = 'actor_movie'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movie.id'))
    actor_id = Column(Integer, ForeignKey('actor.id'))


