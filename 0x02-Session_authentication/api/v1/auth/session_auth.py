#!/usr/bin/env python3
'''docu ment
session auth module
this module contains a SessionAuth class'''
from api.v1.auth.auth import Auth
from models.user import User
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
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''returns a user id based on the session'''
        # print(type(session_id))
        if not session_id:
            return None
        if type(session_id) != str:
            return None
        res = self.user_id_by_session_id.get(session_id)
        return res

    def current_user(self, request=None):
        '''return current user'''
        session_id = self.session_cookie(request)
        user_id = self.user_id_by_session_id.get(session_id)
        user = User.get(user_id)
        return user
