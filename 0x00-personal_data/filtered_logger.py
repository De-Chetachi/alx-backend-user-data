#!/usr/bin/env python3
'''filter data to conceal personnal data'''
from typing import List
import re
import logging
from os import getenv
from mysql.connector import connect
from mysql.connector.connection import MySQLConnection

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''format documentation'''
        log = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log, self.SEPARATOR)


def get_logger() -> logging.Logger:
    '''creates and returns a logger object'''
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(stream_handler)
    return logger


def get_db() -> MySQLConnection:
    '''connect to database'''
    user_ = getenv("PERSONAL_DATA_DB_USERNAME", "root")
    passw = getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host_ = getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = getenv("PERSONAL_DATA_DB_NAME")
    return connect(
            user=user_, password=passw, host=host_, database=db_name
            )
