""" Base module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model for a database table named users.
    Attributes:
        id (Integer): The user's id. It serves as the primary key.
        email (String): The user's email. It cannot be null.
        hashed_password (String): The user's hashed password. It can't be null.
        session_id (String): The user's session id. It can be null.
        reset_token (String): The user's reset token. It can be null.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
