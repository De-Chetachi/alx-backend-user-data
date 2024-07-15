#!/usr/bin/env python3
'''filter data to conceal personnal data'''

from typing import List
import re

def filter_datum(fields: List, redaction: str, message: str, seperator: str) -> str:
    '''obfuscates(make obscure unintelligible) data
    params:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing which character is separating all fields in the log line (message)
    '''
    for field in fields:
        pattern = field + "=(?P<pd>.*?)" + seperator
        p_data = re.search(pattern, message).group("pd")
        message = re.sub(p_data, redaction, message)
    return message
