#!/usr/bin/env python3
"""
Auth module for the user authentication
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Type
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _generate_uuid(self) -> str:
        """Generate a new UUID
        """
        return str(uuid.uuid4())

    def create_session(self, email: str) -> str:
        """Create a new session
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = self._generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy a session
        """
        if user_id is None:
            return None

        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
        If the user exists, generate a UUID and update the user’s reset_token
        database field. Return the token.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("User doesn't exist")

        reset_token = str(uuid.uuid4())
        self._db.update_user(user.id, reset_token=reset_token)

        return reset_token

    def get_user_from_session_id(self, session_id: str) -> Type[User]:
        """Get user from session ID
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def register_user(self, email: str, password: str) -> User:
        """Register a user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            user = self._db.add_user(email, hashed_password)

        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def update_password(self, reset_token: str, password: str) -> None:
        """
        If the reset_token corresponds to a user, hash the password and update
        the user’s hashed_password field with the new hashed password and the
        reset_token field to None.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError("Invalid reset token")

        hashed_password = self._hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=hashed_password, reset_token=None)
