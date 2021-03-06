import datetime
import logging
logger = logging.getLogger(__name__)

from sqlalchemy.orm import exc
from sqlalchemy import or_

from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config, view_defaults

from ..models import User, Page, PageHit

class PageViews:

    def __init__(self, request):
        self.request = request


        self.path = request.params.get('path', None)

        self.title = request.params.get('title', None)
        self.body = request.params.get('body', None)

        self.pages = request.dbsession.query(Page)\
            .all()

        path = request.matchdict.get('path')
        page_id = request.matchdict.get('page_id')

        page = None

        if path or page_id:
            try:
                self.page = request.dbsession.query(Page)\
                    .filter(
                        or_(
                            Page.path == path,
                            Page.id == page_id,
                        )
                    )\
                    .one()


                if path:
                    self.log_page_visit(page)
            except exc.NoResultFound as e:
                raise HTTPNotFound

    def log_page_visit(self, page):
        page_hit = PageHit(
            page_id=self.page.id,
            ip_address=self.request.remote_addr,
        )

        self.request.dbsession.add(page_hit)
        logger.info(f'Viewed page /{self.page.path}')

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

    @view_config(route_name='page.index', renderer='../templates/page/index.jinja2', permission='administrate')
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
        request.dbsession.flush()

        request.session.flash(f'INFO: Added page {p.path}')
        return HTTPFound(request.route_url('page.view', page_id=p.id))

    @view_config(route_name='page.update', request_method='POST', permission='administrate')
    def page_update(self):
        request = self.request

        self.page.path = self.path
        self.page.title = self.title
        self.page.body = self.body.strip()
        self.page.updated_by = request.authenticated_userid
        self.page.updated_on = datetime.datetime.now()

        request.session.flash(f'INFO: Updated page {self.page.path}')
        return HTTPFound(request.route_url('page.view', page_id=self.page.id))

    @view_config(route_name='page.delete', permission='administrate')
    def page_delete(self):
        request = self.request

        try:
            page_hits = request.dbsession.query(PageHit)\
                .filter(PageHit.page_id == self.page.id)\
                .all()

            for page in page_hits:
                request.dbsession.delete(page)

            request.dbsession.flush()

            request.dbsession.delete(self.page)
            request.dbsession.flush()

            request.session.flash(f'INFO: Deleted page')
        except Exception as e:
            logger.error(str(e))    

        return HTTPFound(request.route_url('page.index'))
