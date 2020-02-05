import os
import datetime
import logging
logger = logging.getLogger(__name__)

from msumc.app.functions import file

from sqlalchemy.orm import exc
from sqlalchemy import func

from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from msumc.app.models.user import User
from msumc.app.models.family import Family
from msumc.app.models.person import Person

@view_defaults(permission='administrate')
class FamilyViews:
    def __init__(self, request):
        self.request = request
        self.image_base_dir = f'{os.getcwd()}/msumc/app/static/img/family/'

        family_id = request.matchdict.get('family_id')

        married_on = request.parameters.get('married_on', None)
        self.last_name = request.parameters.get('last_name', None)
        self.married_on = datetime.datetime.strptime(married_on, '%m/%d/%Y') if married_on is not None else None
        self.street1 = request.parameters.get('street1', None)
        self.street2 = request.parameters.get('street2', None)
        self.city = request.parameters.get('city', None)
        self.state = request.parameters.get('state', None)
        self.zipcode = request.parameters.get('zipcode', None)
        self.photo = request.parameters.get('photo', None)
        self.notes = request.parameters.get('notes', None)
        self.photo = request.parameters.get('photo', None)

        self.photo_fp = None
        if self.photo != b'':
            self.photo_fp = file.write_file(self.image_base_dir, self.photo)

        self.family = None
        if family_id:
            try:
                self.family = request.dbsession.query(Family)\
                    .filter(Family.id == family_id)\
                    .one()
            except exc.NoResultFound as e:
                raise HTTPNotFound

    @view_config(route_name='family.index', renderer='../templates/family/index.jinja2')
    def family_index(self):
        request = self.request

        families = request.dbsession.query(Family)\
            .order_by(Family.last_name)\
            .all()

        family_count = request.dbsession.query(Family.id, func.count(Person.id))\
            .select_from(Family)\
            .join(Person, Family.id == Person.family_id)\
            .group_by(Family.last_name)\
            .all()

        family_count = { family_id: count for family_id, count in family_count }

        return {
            'families': families,
            'family_count': family_count,
        }

    @view_config(route_name='family.view', renderer='../templates/family/view.jinja2')
    def family_view(self):
        request = self.request

        try:
            family_id = request.matchdict.get('family_id')

            family = request.dbsession.query(Family)\
                .filter(Family.id == family_id)\
                .one()

            people = request.dbsession.query(Person)\
                .filter(Person.family_id == family_id)\
                .order_by(Person.first_name)\
                .all()

            adults_parents = [person for person in people if not person.is_child]
            children = [person for person in people if person.is_child]

            return {
                'family': family,
                'people': people,
                'adults_parents': adults_parents,
                'children': children,
            }
        except exc.NoResultFound as e:
            raise HTTPNotFound

    @view_config(route_name='family.add', renderer='../templates/family/add.jinja2')
    def family_add_GET(self):
        request = self.request

        return {
        }

    @view_config(route_name='family.add', request_method="POST")
    def family_add_POST(self):
        request = self.request

        family = Family(
            last_name=self.last_name,
            married_on=self.married_on,
            street1=self.street1,
            street2=self.street2,
            city=self.city,
            state=self.state,
            zipcode=self.zipcode,
            notes=self.notes,
            photo_fp=self.photo_fp,
            created_on=datetime.datetime.now(),
            created_by=request.authenticated_userid,
        )

        request.dbsession.add(family)
        request.dbsession.flush()

        request.session.flash('INFO: Added family')
        return HTTPFound(request.route_url('family.view', family_id=family.id))

    @view_config(route_name='family.update', request_method="POST")
    def family_update(self):
        request = self.request

        self.family.last_name = self.last_name
        self.family.married_on = self.married_on
        self.family.street1 = self.street1
        self.family.street2 = self.street2
        self.family.city = self.city
        self.family.state = self.state
        self.family.zipcode = self.zipcode
        self.family.notes = self.notes

        if self.photo != b'':
            file.remove_file(self.family.photo_fp) # remove the old file from the system
            photo_fp = file.write_file(self.image_base_dir, self.photo) # add the new file to the system

            self.family.photo_fp = photo_fp

        request.session.flash('INFO: Updated family')
        return HTTPFound(request.route_url('family.view', family_id=self.family.id))

    @view_config(route_name='family.delete')
    def family_delete(self):
        request = self.request

        try:
            family_id = request.matchdict.get('family_id')

            query = request.dbsession.query(Family)\
                .filter(Family.id == family_id)

            family = query.one() # ensure non-404, will error out if not found

            file.remove_file(family.photo_fp) # remove the old file from the system

            # Delete people
            request.dbsession.query(Person)\
                .filter(Person.family_id == family.id)\
                .delete()

            # Delete Family
            query.delete()

            request.session.flash('INFO: Deleted family')
            return HTTPFound(request.route_url('family.index'))
        except exc.NoResultFound as e:
            raise HTTPNotFound
        except Exception as e:
            raise e
