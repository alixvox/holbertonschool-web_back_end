#!/usr/bin/env python3
""" DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


from user import User, Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user instance to the session DB
        """
        if not email or not hashed_password:
            return None
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        try:
            self._session.commit()
        except SQLAlchemyError:
            self._session.rollback()
            raise
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user instance in the session DB
        """
        if not kwargs:
            raise InvalidRequestError

        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
        except InvalidRequestError:
            raise

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user instance in the session DB
        """
        if not kwargs:
            return None

        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise

        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError

        self._session.commit()
