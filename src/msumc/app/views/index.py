import logging
logger = logging.getLogger(__name__)

from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound

from ..functions.email import send_email

from msumc.app.models.user import User

class IndexViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='index.index')
    def index_index(self):
        request = self.request

        return HTTPFound(request.route_url('page.view_page', path='index'))
