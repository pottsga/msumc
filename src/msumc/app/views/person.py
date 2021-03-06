import os
import datetime
import logging
logger = logging.getLogger(__name__)

from msumc.app.functions import file

from sqlalchemy.orm import exc

from pyramid.view import view_config, view_defaults

from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from msumc.app.models import User, Household, Person

@view_defaults(permission='view_directory')
class PersonViews:
    def __init__(self, request):
        self.request = request

        self.image_base_dir = f'{os.getcwd()}/msumc/app/static/img/person/'

        household_id = request.parameters.get('household_id', None)
        person_id = request.matchdict.get('person_id', None)

        is_active = request.parameters.get('is_active', None)
        is_admin = request.parameters.get('is_admin', None)
        is_deceased = request.parameters.get('is_deceased', None)
        birthday = request.parameters.get('birthday', None)

        self.photo = request.parameters.get('photo', b'')
        self.is_active = True if is_active == 'on' else False
        self.is_admin = True if is_admin == 'on' else False
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

        print(self.photo)
            
        self.photo_fp = None
        if self.photo != b'':
            self.photo_fp = file.write_file(self.image_base_dir, self.photo)

        # If the email is changed, the email is no longer verified
        #   and also delete the User record if it exists
        if self.email != request.parameters.get('email'):
            self.is_email_verified = False

            user = request.dbsession.query(User)\
                .filter(User.email == self.email)\
                .first()

            if user:
                request.dbsession.delete(user)

        # Un-admin the user when the 'is_admin' flag is set to false
        if self.is_admin == False:
            user = request.dbsession.query(User)\
                .filter(User.email == self.email)\
                .first()

            if user:
                user.groups = ['group:members']

        self.households = request.dbsession.query(Household)\
            .order_by(Household.last_name)\
            .all()

        self.people = request.dbsession.query(Person)\
            .all()

        self.households_by_id = {
            household.id: household
            for household in self.households
        }

        self.households_and_people = {
            household: [ person.first_name for person in self.people if person.household_id == household.id ]
            for household in self.households
        }

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

                if self.person.is_email_verified:
                    user = request.dbsession.query(User)\
                        .filter(User.email == self.person.email)\
                        .first()

                    # user.groups = ['group:admins']

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
            'households_by_id': self.households_by_id,
        }

    @view_config(route_name='person.view', renderer='../templates/person/view.jinja2')
    def person_view(self):
        request = self.request

        return {
            'person': self.person,
            'household': self.household,
            'households': self.households,
        }

    @view_config(route_name='person.add', renderer='../templates/person/add.jinja2', request_method='GET', permission='administrate')
    def person_add_GET(self):
        request = self.request

        return {
            'households_and_people': self.households_and_people,
            'household_id': self.household_id,
            'households': self.households,
            'household': self.household,
        }

    @view_config(route_name='person.add', request_method='POST', permission='administrate')
    def person_add_POST(self):
        request = self.request

        # Check if email already in use by another account
        email_exists = True if len(request.dbsession.query(Person).filter(Person.email == self.email).all()) > 0 and self.email is not None else False

        if email_exists:
            request.session.flash('ERROR: Email already is in use by another account, please use a unique email.')
            return HTTPFound(request.route_url('person.add'))

        print(self.photo_fp)

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
            photo_fp=self.photo_fp,
            created_on=datetime.datetime.now(),
            created_by=request.authenticated_userid,
        )
        request.dbsession.add(person)
        request.dbsession.flush()

        request.session.flash('INFO: Added person')
        return HTTPFound(request.route_url('household.view', household_id=person.household_id))

    @view_config(route_name='person.update', request_method='POST', permission='administrate')
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
        self.person.is_admin = self.is_admin

        if self.photo != b'':
            file.remove_file(self.person.photo_fp) # remove the old file from the system
            photo_fp = file.write_file(self.image_base_dir, self.photo) # add the new file to the system

            self.person.photo_fp = photo_fp

        request.session.flash('INFO: Updated person')
        return HTTPFound(request.route_url('person.view', person_id=self.person.id))

    @view_config(route_name='person.delete', permission='administrate')
    def person_delete(self):
        request = self.request

        try:

            # Delete person
            query = request.dbsession.query(Person)\
                .filter(Person.id == self.person.id)\
                .delete()

            request.dbsession.flush()

            # Delete the user
            user = request.dbsession.query(User)\
                .filter(User.email == self.person.email)\
                .delete()
            request.dbsession.flush()
        except Exception as e:
            logger.error(str(e))

        request.session.flash('INFO: Deleted person')
        return HTTPFound(request.route_url('household.view', household_id=self.person.household_id))
