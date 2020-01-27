from sqlalchemy.orm import exc

from pyramid.httpexceptions import HTTPFound, HTTPBadRequest
from pyramid.security import remember, forget
from pyramid.view import view_config

from directory.security import hash_password, check_password

import logging
logger = logging.getLogger(__name__)

from directory.app.models.user import User

class AuthViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='auth.login', renderer='../templates/auth/login.jinja2', request_method="GET")
    def auth_login_GET(self):
        request = self.request

        return {
        }

    @view_config(route_name='auth.login', request_method="POST")
    def auth_login_POST(self):
        request = self.request

        username = request.params.get('username', None)
        password = request.params.get('password', None)

        try:
            user = request.dbsession.query(User)\
                .filter(User.username == username)\
                .one()

            password_matches = check_password(password, user.password)

            if not password_matches:
                raise ValueError('Password incorrect')

            headers = remember(request, user.username)
            request.session.flash(f'INFO: Welcome, {user.username}')
            return HTTPFound(request.route_url('admin.index'), headers=headers)
        except exc.NoResultFound as e:
            request.session.flash(f'ERROR: No username found in the database.')
            return HTTPFound(request.route_url('auth.login'))
        except ValueError as e:
            error = str(e)

            if error == 'Password incorrect':
                request.session.flash(f'ERROR: Incorrect password.')
                return HTTPFound(request.route_url('auth.login'))

    @view_config(route_name='auth.logout', request_method="GET")
    def auth_logout(self):
        request = self.request
        headers = forget(request)

        return HTTPFound(request.route_url('index.index'), headers=headers)
