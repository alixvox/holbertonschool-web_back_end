#!/usr/bin/env python3
"""
BasicAuth module
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import Tuple, TypeVar, Optional


class BasicAuth(Auth):
    """
    BasicAuth class
    """

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the User instance for a request.

        Args:
            request (Request): Flask request object (default: None).

        Returns:
            TypeVar('User'): The User instance if
            authenticated, None otherwise.
        """
        if not request:
            return None
        header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(header)
        decoded_header = self.decode_base64_authorization_header(base64_header)
        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(user_email, user_pwd)

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            return message_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization header
        """

        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def extract_user_credentials(
            self, decoded_base64_authorization_header: Optional[str]
            ) -> Tuple[Optional[str], Optional[str]]:
        """
        returns the user email and password from the Base64 decoded value
        """

        if (decoded_base64_authorization_header is None or
                type(decoded_base64_authorization_header) is not str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(":", 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self, user_email: Optional[str], user_pwd: Optional[str]
            ) -> TypeVar('User'):
        """Returns the User instance based on email and password.

        Args:
            user_email (str): Email of the user.
            user_pwd (str): Password of the user.

        Returns:
            TypeVar('User'): The User instance if found, None otherwise.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None
