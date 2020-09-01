from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, String, DateTime

from .base import db


class Questionnare(db.Model):
    __tablename__ = 'questionnare'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, unique=False, default=datetime.now())
    name = Column(String, unique=False)
    address = Column(String, unique=False)
    occupation = Column(String, unique=False)
    children = Column(Boolean, unique=False)
    num_children = Column(Integer)
    email = Column(String, unique=True)
