import logging
logger = logging.getLogger(__name__)

from pyramid.view import view_config, view_defaults

from directory.app.models.user import User

class IndexViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='index.index', renderer='../templates/index/index.jinja2')
    def index_index(self):
        request = self.request

        return {
        }
