from api.models.base import db
from sqlalchemy import Column, Integer, Float, Boolean, String, DateTime


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
