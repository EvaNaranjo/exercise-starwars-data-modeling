import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    active = Column(Boolean)
    create = Column(DateTime)
    update = Column(DateTime)

class Planet (Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    terrain = Column(String(250))
    active = Column(Boolean)
    create = Column(DateTime)
    update = Column(DateTime)

class Character (Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    description = Column(String(250))
    eye_color = Column(String(250))
    id_planet = Column(Integer, ForeignKey("planet.id"))
    planet = relationship(Planet)
    active = Column(Boolean)
    create = Column(DateTime)
    update = Column(DateTime)

class Favourite(Base):
    __tablename__ = 'favourite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    id_planet = Column(Integer, ForeignKey("planet.id"))
    planet = relationship(Planet)
    id_character = Column(Integer, ForeignKey("character.id"))
    chacater = relationship(Character)
    create = Column(DateTime)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')