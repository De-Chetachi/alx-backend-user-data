#!/usr/bin/env python3
'''authentication module'''
from flask import request
from typing import List, TypeVar


class Auth:
    '''my auth class'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''require authentication'''
        if not path or not excluded_paths or not len(excluded_paths):
            return True
        for path_ in excluded_paths:
            if path_.endswith('*') and path.startswith(path[:-1]):
                return False

        if not path.endswith('/'):
            path = path + '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        '''require authentication'''
        if not request:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        '''retrive user making a request'''
        return None
