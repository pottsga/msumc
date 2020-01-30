import logging
logger = logging.getLogger(__name__)

from pyramid.view import view_config, view_defaults

from msumc.app.models.user import User

class ContactViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='contact.index', renderer='../templates/contact/index.jinja2')
    def contact_index(self):
        request = self.request

        return {
        }
