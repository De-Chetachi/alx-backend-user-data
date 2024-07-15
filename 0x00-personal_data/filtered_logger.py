#!/usr/bin/env python3
'''filter data to conceal personnal data'''
from typing import List
import re


def filter_datum(
        fields: List[str], redaction: str, message: str, seperator: str
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
        pattern = field + f"=.*?{seperator}"
        message = re.sub(pattern, field + "=" + redaction + seperator, message)
    return message
