#!/usr/bin/env python3
'''filter data to conceal personnal data'''
from typing import List
import re
import logging


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    '''obfuscates(make obscure unintelligible) data
    params:
        fields: a list of strings representing all fields to obfuscate
        redaction a string representing by what the field will be obscured
        message a string representing the log line
        seperator: a string representing which character is separating
        all fields in the log line (message)
    '''
    for field in fields:
        pattern = field + f"=.*?{separator}"
        message = re.sub(pattern, field + "=" + redaction + separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields;

    def format(self, record: logging.LogRecord) -> str:
        log = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log, self.SEPARATOR)
