#!/usr/bin/env python3
"""
Module for hashing a password.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password, which is a byte string.

    Args:
    - password: string type
    """

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if a password is valid.

    Args:
    - hashed_password: bytes type
    - password: string type
    """

    return bcrypt.checkpw(password.encode(), hashed_password)
