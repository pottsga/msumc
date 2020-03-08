import logging
logger = logging.getLogger(__name__)

from pyramid.view import view_config, view_defaults

from sqlalchemy import func, desc

from ..models import PageHit, Page, Person

@view_defaults(permission='administrate')
class AdminViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='admin.index', renderer='../templates/admin/index.jinja2')
    def admin_index(self):
        request = self.request

        page_hits = request.dbsession.query(Page, func.count(PageHit.page_id).label('count'))\
            .select_from(PageHit)\
            .outerjoin(Page, Page.id == PageHit.page_id)\
            .group_by(PageHit.page_id)\
            .order_by(desc('count'))\
            .all()

        verified_people = request.dbsession.query(Person)\
            .filter(Person.is_email_verified == True)\
            .order_by(Person.last_name)\
            .all()

        return {
            'page_hits': page_hits,
            'verified_people': verified_people,
        }
