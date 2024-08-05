#!/usr/bin/env python3
'''basic uth module'''
from api.v1.auth.auth import Auth
from base64 import b64decode
import binascii


class BasicAuth(Auth):
    '''a basic auth class inherits fron auth above'''
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        ''' returns the Base64 part of the Authorization header'''
        if not authorization_header:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.replace('Basic ', '')

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''eturns the decoded value of a Base64 string
        base64_authorization_header'''
        if not base64_authorization_header:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            return b64decode(base64_authorization_header).decode()
        except binascii.Error:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        '''returns the user email and password from the Base64 decoded value'''
        if not decoded_base64_authorization_header:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':'))
