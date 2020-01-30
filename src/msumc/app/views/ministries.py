import logging
logger = logging.getLogger(__name__)

from pyramid.view import view_config, view_defaults

from msumc.app.models.user import User
from msumc.app.models.ministry import Ministry

class MinistriesViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='ministry.view_all', renderer='../templates/ministry/view_all.jinja2')
    def ministry_view_all(self):
        request = self.request

        ministries = request.dbsession.query(Ministry)\
            .filter(Ministry.active == True)\
            .order_by(Ministry.title)\
            .all()

        return {
            'ministries': ministries,
        }

    @view_config(route_name='ministry.index', renderer='../templates/ministry/index.jinja2', permission='administrate')
    def ministry_index(self):
        request = self.request

        return {
        }

