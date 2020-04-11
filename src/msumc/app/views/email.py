import datetime
import logging
import os
import io
import tempfile

from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPBadRequest
from pyramid.response import FileResponse, Response
from pyramid.view import view_config, view_defaults
from sqlalchemy import func, desc
from sqlalchemy.orm import exc

from msumc.app.functions import file
from msumc.app.models import Household, Person, Upload, User

logger = logging.getLogger(__name__)

@view_defaults(permission='administrate')
class DirectoryViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='email.index', renderer='../templates/email/index.jinja2')
    def email_index(self):
        request = self.request

        people = request.dbsession.query(Person)\
            .filter(
                Person.is_active == True,
                Person.email != None
            )\
            .order_by(Person.email)\
            .all()

        emails = [person.email for person in people]

        return {
            'emails': emails,
        }
