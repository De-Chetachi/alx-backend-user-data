#!/usr/bin/env python3
'''filter data to conceal personnal data'''
from typing import List
import re


def filter_datum(fields: List[str], red: str, msg: str, delim: str) -> str:
    '''obfuscates(make obscure unintelligible) data
    params:
        fields: a list of strings representing all fields to obfuscate
        red: redaction a string representing by what the field will be obscured
        msg: message a string representing the log line
        delim: a string representing which character is separating
        all fields in the log line (message)
    '''
    for field in fields:
        p_data = re.search(field + "=(?P<pd>.*?)" + delim, msg).group("pd")
        msg = re.sub(p_data, red, msg)
    return msg
