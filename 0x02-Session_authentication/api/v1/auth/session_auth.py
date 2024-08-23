#!/usr/bin/env python3
'''docu ment
session auth module
this module contains a SessionAuth class'''
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    '''inherits from auth'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''creates a session id and stores it'''
        if not user_id:
            return None
        if type(user_id) != str:
            return None
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
