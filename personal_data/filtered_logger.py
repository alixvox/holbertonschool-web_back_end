#!/usr/bin/env python3
"""
This module provides a function filter_datum that obfuscates
specific fields in a log message.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Use regex to replace occurrences of certain field values in a log message.

    Args:
        fields (List[str]): A list of fields to obfuscate.
        redaction (str): A string representing the redaction.
        message (str): A string representing the log line.
        separator (str): A string representing the
        separator character in the log line.

    Returns:
        str: The obfuscated log message.
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
