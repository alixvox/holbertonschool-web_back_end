#!/usr/bin/env python3
"""
filtered_logger.py
This module provides functionality for obfuscating sensitive information
in log messages. It includes a function for filtering data fields and a
custom log formatter class for integrating this functionality into the
Python logging system.
"""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): A list of fields to obfuscate.
        redaction (str): A string representing the redaction.
        message (str): A string representing the log line.
        separator (str): A string representing the separator character
        in the log line.

    Returns:
        str: The obfuscated log message.
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message.rstrip(separator)


class RedactingFormatter(logging.Formatter):
    """
    Formatter class for logging module with redaction capability.

    This formatter redacts specific fields in the log messages it formats.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize RedactingFormatter with fields to redact.

        Args:
            fields (List[str]): Fields to redact in the log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format log record, redacting specified fields.

        Args:
            record (logging.LogRecord): Log record.

        Returns:
            str: Formatted log record with specified fields redacted.
        """
        original_msg = logging.Formatter.format(self, record)
        return filter_datum(self.fields, self.REDACTION,
                            original_msg, self.SEPARATOR)
