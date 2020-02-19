import os
import datetime
import logging
logger = logging.getLogger(__name__)

from msumc.app.functions import file

from sqlalchemy.orm import exc
from sqlalchemy import func

from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from msumc.app.models import (
    User,
    Household,
    Person,
    Upload,
)

@view_defaults(permission='administrate')
class HouseholdViews:
    def __init__(self, request):
        self.request = request
        self.upload_base_dir = f'{os.getcwd()}/msumc/app/static/uploads/'

        upload_id = request.matchdict.get('upload_id')
        self.upload = request.parameters.get('upload', None)

        self.upload_fp = None
        if self.upload != b'':
            self.upload_fp = file.write_file(self.upload_base_dir, self.upload)

        self.upload = None
        if upload_id:
            try:
                self.upload = request.dbsession.query(Upload)\
                    .filter(Upload.id == upload_id)\
                    .one()
            except exc.NoResultFound as e:
                raise HTTPNotFound


    @view_config(route_name='upload.index', renderer='../templates/upload/index.jinja2')
    def upload_index(self):
        request = self.request

        uploads = self.request.dbsession.query(Upload)\
            .all()

        return {
            'uploads': uploads,
        }

    @view_config(route_name='upload.add', renderer='../templates/upload/add.jinja2')
    def upload_add_GET(self):
        request = self.request

        return {
        }

    @view_config(route_name='upload.add', request_method="POST")
    def upload_add_POST(self):
        request = self.request

        upload = Upload(
            fp=self.upload_fp,
            created_on=datetime.datetime.now(),
            created_by=request.authenticated_userid,
        )

        request.dbsession.add(upload)
        request.dbsession.flush()

        request.session.flash('INFO: Added upload')
        return HTTPFound(request.route_url('upload.view', upload_id=upload.id))

    @view_config(route_name='upload.view', renderer='../templates/upload/view.jinja2')
    def upload_view(self):
        request = self.request

        return {
            'upload': self.upload,
        }

    @view_config(route_name='upload.delete')
    def upload_delete(self):
        request = self.request

        try:
            upload_id = request.matchdict.get('upload_id')

            query = request.dbsession.query(Upload)\
                .filter(Upload.id == upload_id)

            upload = query.one() # ensure non-404, will error out if not found

            file.remove_file(upload.fp) # remove the old file from the system

            # Delete upload
            query.delete()

            request.session.flash('INFO: Deleted upload')
            return HTTPFound(request.route_url('upload.index'))
        except exc.NoResultFound as e:
            raise HTTPNotFound
        except Exception as e:
            raise e
