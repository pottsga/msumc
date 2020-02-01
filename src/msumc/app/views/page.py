import datetime
import logging
logger = logging.getLogger(__name__)

from sqlalchemy.orm import exc

from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config, view_defaults

from msumc.app.models.user import User
from msumc.app.models.page import Page

class PageViews:

    def __init__(self, request):
        self.request = request

        self.path = request.params.get('path', None)
        self.title = request.params.get('title', None)
        self.body = request.params.get('body', None)

        self.pages = request.dbsession.query(Page)\
            .all()

        path = request.matchdict.get('path')

        if path:
            try:
                self.page = request.dbsession.query(Page)\
                    .filter(Page.path == path)\
                    .one()
            except exc.NoResultFound as e:
                raise HTTPNotFound

    def path_exists_already(self, path):
        path_exists = self.request.dbsession.query(Page)\
            .filter(Page.path == path)\
            .first()

        return True if path_exists else False

    @view_config(route_name='page.view_page', renderer='../templates/page/view_page.jinja2')
    def page_view_page(self):
        request = self.request

        return {
            'page': self.page,
            'title': self.page.title,
        }

    @view_config(route_name='page.index', renderer='../templates/page/index.jinja2')
    def page_index(self):
        request = self.request

        return {
            'pages': self.pages,
        }

    @view_config(route_name='page.view', renderer='../templates/page/view.jinja2', permission='administrate')
    def page_view(self):
        request = self.request

        return {
            'page': self.page,
        }

    @view_config(route_name='page.add', renderer='../templates/page/add.jinja2', request_method='GET', permission='administrate')
    def page_add_GET(self):
        request = self.request

        return {
        }

    @view_config(route_name='page.add', request_method='POST', permission='administrate')
    def page_add_POST(self):
        request = self.request

        path_exists_already = self.path_exists_already(self.path)

        if path_exists_already:
            request.session.flash('ERROR: Path already exists in the database. Try again with another path')
            return HTTPFound(request.route_url('page.add'))

        p = Page(
            path=self.path,
            title=self.title,
            body=self.body.strip(),
            created_by=request.authenticated_userid,
            created_on=datetime.datetime.now(),
        )
        request.dbsession.add(p)

        request.session.flash(f'INFO: Added page {p.path}')
        return HTTPFound(request.route_url('page.view', path=p.path))

    @view_config(route_name='page.update', request_method='POST', permission='administrate')
    def page_update(self):
        request = self.request

        self.page.path = self.path
        self.page.title = self.title
        self.page.body = self.body.strip()
        self.page.updated_by = request.authenticated_userid
        self.page.updated_on = datetime.datetime.now()

        request.session.flash(f'INFO: Updated page {self.page.path}')
        return HTTPFound(request.route_url('page.view', path=self.page.path))
