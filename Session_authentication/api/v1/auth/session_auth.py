#!/usr/bin/env python3
"""
BasicAuth module
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import Tuple, TypeVar, Optional


class SessionAuth(Auth):
    pass
