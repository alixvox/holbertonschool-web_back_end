#!/usr/bin/env python3
"""
Auth module
"""
from os import getenv
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required
        Args:
            path: string type
            excluded_paths: list of string types
        Returns:
            bool: False if path is in the list of excluded_paths
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Checks if the request is authorized
        Args:
            request: request object
        Returns:
            str: None if the request is not authorized
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user
        Args:
            request: request object
        Returns:
            TypeVar('User'): None for this method
        """
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
