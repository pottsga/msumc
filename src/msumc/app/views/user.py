import logging
logger = logging.getLogger(__name__)

from pyramid.view import view_config, view_defaults

from ..models import User

@view_defaults(permission='administrate')
class UserViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='user.index', renderer='../templates/user/index.jinja2')
    def user_index(self):
        request = self.request

        users = request.dbsession.query(User).all()

        return {
            'users': users,
        }
