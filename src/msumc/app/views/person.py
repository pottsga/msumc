import datetime
import logging
logger = logging.getLogger(__name__)

from sqlalchemy.orm import exc

from pyramid.view import view_config, view_defaults

from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from msumc.app.models.user import User
from msumc.app.models.household import Household
from msumc.app.models.person import Person

@view_defaults(permission='administrate')
class PersonViews:
    def __init__(self, request):
        self.request = request

        household_id = request.parameters.get('household_id', None)
        person_id = request.matchdict.get('person_id', None)

        is_active = request.parameters.get('is_active', None)
        is_deceased = request.parameters.get('is_deceased', None)
        birthday = request.parameters.get('birthday', None)

        self.is_active = True if is_active == 'on' else False
        self.is_deceased = True if is_deceased == 'on' else False
        self.household_id = int(household_id) if household_id else None
        self.first_name = request.parameters.get('first_name', None)
        self.familial_relationship = request.parameters.get('familial_relationship', None)
        self.last_name = request.parameters.get('last_name', None)
        self.position = request.parameters.get('position', None)
        self.gender = request.parameters.get('gender', None)
        self.birthday = datetime.datetime.strptime(birthday, '%m/%d/%Y') if birthday is not None else None
        self.phone_number = request.parameters.get('phone_number', None)
        self.email = request.parameters.get('email', None)
        self.notes = request.parameters.get('notes', None)
        self.people = request.dbsession.query(Person)\
            .all()

        self.households = request.dbsession.query(Household)\
            .all()

        self.household = None
        if household_id:
            try:
                self.household = request.dbsession.query(Household)\
                    .filter(Household.id == household_id)\
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
                self.household = request.dbsession.query(Household)\
                    .filter(Household.id == self.person.household_id)\
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
            'household_id': self.household_id,
            'households': self.households,
            'household': self.household,
        }

    @view_config(route_name='person.add', request_method='POST')
    def person_add_POST(self):
        request = self.request

        person = Person(
            is_active=self.is_active,
            is_deceased=self.is_deceased,
            household_id=self.household_id,
            familial_relationship=self.familial_relationship,
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
        return HTTPFound(request.route_url('household.view', household_id=person.household_id))

    @view_config(route_name='person.view', renderer='../templates/person/view.jinja2')
    def person_view(self):
        request = self.request

        return {
            'person': self.person,
            'household': self.household,
            'households': self.households,
        }

    @view_config(route_name='person.update', request_method='POST')
    def person_update_POST(self):
        request = self.request

        self.person.is_active = self.is_active
        self.person.is_deceased = self.is_deceased
        self.person.household_id = self.household_id
        self.person.familial_relationship = self.familial_relationship
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
        return HTTPFound(request.route_url('household.view', household_id=self.person.household_id))
