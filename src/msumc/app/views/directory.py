import datetime
import logging
import os
import io
import tempfile

import jinja2
import weasyprint
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPBadRequest
from pyramid.response import FileResponse, Response
from pyramid.view import view_config, view_defaults
from sqlalchemy import func, desc
from sqlalchemy.orm import exc

from msumc.app.functions import file
from msumc.app.models import Household, Person, Upload, User

logger = logging.getLogger(__name__)


@view_defaults(permission='view_directory')
class DirectoryViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='directory.index', renderer='../templates/directory/index.jinja2')
    def directory_index(self):
        request = self.request

        uploads = self.request.dbsession.query(Upload)\
            .all()

        return {
            'uploads': uploads,
        }

    @view_config(route_name='directory.pdf')
    def directory_pdf(self):
        request = self.request

        households = request.dbsession.query(Household)\
            .order_by(Household.last_name)\
            .all()
        people = request.dbsession.query(Person)\
            .filter(
                Person.is_active == True,
                Person.is_deceased == False,
            )\
            .order_by(desc(Person.household_id))\
            .all()

        if not households or not people:
            return HTTPBadRequest()

        households_by_id = {
            household.id: household
            for household in households
        }

        template_loader = jinja2.FileSystemLoader(
            searchpath="./msumc/app/templates/directory/pdf/")
        template_env = jinja2.Environment(loader=template_loader)
        TEMPLATE_FILE = "index.jinja2"
        template = template_env.get_template(TEMPLATE_FILE)

        html = template.render({
            'request': request,
            'people': people,
            'households_by_id': households_by_id,
        })

        pdf_file = os.path.join(os.getcwd(), 'msumc/app/static/file/directory.pdf')

        html = weasyprint.HTML(string=html)

        try:
            f = open(pdf_file, 'wb')
            html.write_pdf(f)
        except Exception as e:
            print(str(e))

        return HTTPFound(request.static_url('msumc:app/static/file/directory.pdf'))
