import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id=Column (Integer,primary_key=True)
    username= Column(String (250),nullable=False,unique=True)
    email= Column(String (250),nullable=False,unique=True)
    firstname=Column(String (250),nullable=False)
    lastname=Column(String (250),nullable=False)
    password = Column(String(250), nullable=False)
    fecha_de_suscripcion = Column(String(250), nullable=True)




class Favoritos (Base):
    __tablename__= 'favoritos'
    id=Column (Integer,primary_key=True)
    character_id=Column(Integer,ForeignKey('character.id'))
    planet_id =Column(Integer,ForeignKey('planet.id'))
    user_id =Column(Integer,ForeignKey('user.id'))
    user=relationship(User)
    planet = relationship("Planet")
    character = relationship("Character")

class Planet (Base):
    __tablename__='planet'
    id=Column (Integer,primary_key=True)
    planet=relationship(Favoritos)
    name = Column(String(250), nullable=False) 
    climate = Column(String(250), nullable=True)  
    terrain = Column(String(250), nullable=True)  
    population = Column(Integer, nullable=True) 


class character(Base):
    __tablename__='character'
    id=Column (Integer,primary_key=True)
    name = Column(String(250), nullable=False)  
    gender = Column(String(20), nullable=True) 
    height = Column(Integer, nullable=True)  
    mass = Column(Integer, nullable=True)  
    character=relationship(Favoritos)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
