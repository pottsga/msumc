import logging
logger = logging.getLogger(__name__)

from pyramid.view import view_config, view_defaults

from msumc.app.models.user import User

@view_defaults(permission='administrate')
class AdminViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='admin.index', renderer='../templates/admin/index.jinja2')
    def admin_index(self):
        request = self.request

        return {
        }
