import datetime
import logging
logger = logging.getLogger(__name__)

from sqlalchemy.orm import exc

from pyramid.view import view_config, view_defaults

from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from msumc.app.models.user import User
from msumc.app.models.family import Family
from msumc.app.models.person import Person

class PersonViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='person.index', renderer='../templates/person/index.jinja2')
    def person_index(self):
        request = self.request

        people = request.dbsession.query(Person)\
            .order_by(Person.last_name)\
            .all()

        return {
            'people': people,
        }

    @view_config(route_name='person.add', renderer='../templates/person/add.jinja2', request_method='GET')
    def person_add_GET(self):
        request = self.request

        try:
            family_id = request.parameters.get('family_id', None)

            family = None
            if family_id:
                family = request.dbsession.query(Family)\
                    .filter(Family.id == family_id)\
                    .one()

            families = request.dbsession.query(Family)\
                .order_by(Family.last_name, Family.id)\
                .all()

            return {
                'family_id': family_id,
                'families': families,
                'family': family,
            }
        except exc.NoResultFound as e:
            raise HTTPNotFound
        except Exception as e:
            raise e

    @view_config(route_name='person.add', request_method='POST')
    def person_add_POST(self):
        request = self.request

        try:
            is_child = request.parameters.get('is_child', None)
            is_child = True if is_child == 'on' else False
            family_id = request.parameters.get('family_id', None)
            first_name = request.parameters.get('first_name', None)
            last_name = request.parameters.get('last_name', None)
            position = request.parameters.get('position', None)
            gender = request.parameters.get('gender', None)
            birthday = request.parameters.get('birthday', None)
            birthday = datetime.datetime.strptime(birthday, '%m/%d/%Y') if birthday is not None else None
            phone_number = request.parameters.get('phone_number', None)
            email = request.parameters.get('email', None)
            notes = request.parameters.get('notes', None)

            person = Person(
                is_child=is_child,
                family_id=int(family_id),
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                birthday=birthday,
                phone_number=phone_number,
                email=email,
                notes=notes,
                created_on=datetime.datetime.now(),
                created_by=request.authenticated_userid,
            )
            request.dbsession.add(person)
            request.dbsession.flush()

            request.session.flash('INFO: Added person')
            return HTTPFound(request.route_url('family.view', family_id=person.family_id))
        except Exception as e:
            raise e

    @view_config(route_name='person.view', renderer='../templates/person/view.jinja2')
    def person_view(self):
        request = self.request

        try:
            person_id = request.matchdict.get('person_id')

            person = request.dbsession.query(Person)\
                .filter(Person.id == person_id)\
                .one()

            family = request.dbsession.query(Family)\
                .filter(Family.id == person.family_id)\
                .one()

            families = request.dbsession.query(Family)\
                .order_by(Family.last_name)\
                .all()

            return {
                'person': person,
                'family': family,
                'families': families,
            }
        except exc.NoResultFound as e:
            raise HTTPNotFound

    @view_config(route_name='person.update', request_method='POST')
    def person_update_POST(self):
        request = self.request

        try:
            person_id = request.matchdict.get('person_id')

            is_child = request.parameters.get('is_child', None)
            is_child = True if is_child == 'on' else False
            family_id = request.parameters.get('family_id', None)
            first_name = request.parameters.get('first_name', None)
            last_name = request.parameters.get('last_name', None)
            position = request.parameters.get('position', None)
            gender = request.parameters.get('gender', None)
            birthday = request.parameters.get('birthday', None)
            birthday = datetime.datetime.strptime(birthday, '%m/%d/%Y') if birthday is not None else None
            phone_number = request.parameters.get('phone_number', None)
            email = request.parameters.get('email', None)
            notes = request.parameters.get('notes', None)

            person = request.dbsession.query(Person)\
                .filter(Person.id == person_id)\
                .one()
            
            person.is_child = is_child
            person.family_id = int(family_id)
            person.first_name = first_name
            person.last_name = last_name
            person.gender = gender
            person.phone_number = phone_number
            person.email = email
            person.notes = notes
            person.birthday = birthday

            request.session.flash('INFO: Updated person')
            return HTTPFound(request.route_url('person.view', person_id=person.id))
        except Exception as e:
            raise e

    @view_config(route_name='person.delete')
    def person_delete(self):
        request = self.request

        try:
            person_id = request.matchdict.get('person_id')

            query = request.dbsession.query(Person)\
                .filter(Person.id == person_id)

            person = query.one() # ensure non-404, will error out if not found

            # Delete person
            query.delete()

            request.session.flash('INFO: Deleted person')
            return HTTPFound(request.route_url('family.view', family_id=person.family_id))
        except exc.NoResultFound as e:
            raise HTTPNotFound
        except Exception as e:
            raise e
