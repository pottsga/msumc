import logging
logger = logging.getLogger(__name__)

from pyramid.view import view_config, view_defaults

from directory.app.models.user import User

class AdminViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='admin.index', renderer='../templates/admin/index.jinja2')
    def admin_index(self):
        request = self.request

        return {
        }
