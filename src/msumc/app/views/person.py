import datetime
import logging
logger = logging.getLogger(__name__)

from sqlalchemy.orm import exc

from pyramid.view import view_config, view_defaults

from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from msumc.app.models.user import User
from msumc.app.models.family import Family
from msumc.app.models.person import Person

@view_defaults(permission='administrate')
class PersonViews:
    def __init__(self, request):
        self.request = request

        family_id = request.parameters.get('family_id', None)
        person_id = request.matchdict.get('person_id', None)

        is_child = request.parameters.get('is_child', None)
        is_active = request.parameters.get('is_active', None)
        birthday = request.parameters.get('birthday', None)

        self.is_child = True if is_child == 'on' else False
        self.is_active = True if is_active == 'on' else False
        self.family_id = int(family_id) if family_id else None
        self.first_name = request.parameters.get('first_name', None)
        self.last_name = request.parameters.get('last_name', None)
        self.position = request.parameters.get('position', None)
        self.gender = request.parameters.get('gender', None)
        self.birthday = datetime.datetime.strptime(birthday, '%m/%d/%Y') if birthday is not None else None
        self.phone_number = request.parameters.get('phone_number', None)
        self.email = request.parameters.get('email', None)
        self.notes = request.parameters.get('notes', None)
        self.people = request.dbsession.query(Person)\
            .all()

        self.families = request.dbsession.query(Family)\
            .all()

        self.family = None
        if family_id:
            try:
                self.family = request.dbsession.query(Family)\
                    .filter(Family.id == family_id)\
                    .one()
            except exc.NoResultFound as e:
                raise HTTPNotFound

        self.person = None
        if person_id:
            try:
                self.person = request.dbsession.query(Person)\
                    .filter(Person.id == person_id)\
                    .one()

            except exc.NoResultFound as e:
                raise HTTPNotFound

            try:
                self.family = request.dbsession.query(Family)\
                    .filter(Family.id == self.person.family_id)\
                    .one()
            except exc.NoResultFound as e:
                raise HTTPNotFound

    @view_config(route_name='person.index', renderer='../templates/person/index.jinja2')
    def person_index(self):
        request = self.request

        return {
            'people': self.people,
        }

    @view_config(route_name='person.add', renderer='../templates/person/add.jinja2', request_method='GET')
    def person_add_GET(self):
        request = self.request

        return {
            'family_id': self.family_id,
            'families': self.families,
            'family': self.family,
        }

    @view_config(route_name='person.add', request_method='POST')
    def person_add_POST(self):
        request = self.request

        person = Person(
            is_child=self.is_child,
            is_active=self.is_active,
            family_id=self.family_id,
            first_name=self.first_name,
            last_name=self.last_name,
            gender=self.gender,
            birthday=self.birthday,
            phone_number=self.phone_number,
            email=self.email,
            notes=self.notes,
            created_on=datetime.datetime.now(),
            created_by=request.authenticated_userid,
        )
        request.dbsession.add(person)
        request.dbsession.flush()

        request.session.flash('INFO: Added person')
        return HTTPFound(request.route_url('family.view', family_id=person.family_id))

    @view_config(route_name='person.view', renderer='../templates/person/view.jinja2')
    def person_view(self):
        request = self.request

        return {
            'person': self.person,
            'family': self.family,
            'families': self.families,
        }

    @view_config(route_name='person.update', request_method='POST')
    def person_update_POST(self):
        request = self.request

        self.person.is_child = self.is_child
        self.person.is_active = self.is_active
        self.person.family_id = self.family_id
        self.person.first_name = self.first_name
        self.person.last_name = self.last_name
        self.person.gender = self.gender
        self.person.phone_number = self.phone_number
        self.person.email = self.email
        self.person.notes = self.notes
        self.person.birthday = self.birthday

        request.session.flash('INFO: Updated person')
        return HTTPFound(request.route_url('person.view', person_id=self.person.id))

    @view_config(route_name='person.delete')
    def person_delete(self):
        request = self.request

        # Delete person
        query = request.dbsession.query(Person)\
            .filter(Person.id == self.person.id)\
            .delete()

        request.session.flash('INFO: Deleted person')
        return HTTPFound(request.route_url('family.view', family_id=self.person.family_id))
