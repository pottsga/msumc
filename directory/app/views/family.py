import datetime
import logging
logger = logging.getLogger(__name__)

from sqlalchemy.orm import exc
from sqlalchemy import func

from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from directory.app.models.user import User
from directory.app.models.family import Family
from directory.app.models.person import Person

@view_defaults(permission='administrate')
class FamilyViews:

    def __init__(self, request):
        self.request = request

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

        print(family_count)

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

        try:
            last_name = request.parameters.get('last_name', None)
            married_on = request.parameters.get('married_on', None)
            married_on = datetime.datetime.strptime(married_on, '%m/%d/%Y') if married_on is not None else None
            street1 = request.parameters.get('street1', None)
            street2 = request.parameters.get('street2', None)
            city = request.parameters.get('city', None)
            state = request.parameters.get('state', None)
            zipcode = request.parameters.get('zipcode', None)
            photo = request.parameters.get('photo', None)
            notes = request.parameters.get('notes', None)
            active = request.parameters.get('active', None)
            active = True if active == 'on' else False

            #TODO: Add photo

            family = Family(
                active=active,
                last_name=last_name,
                married_on=married_on,
                street1=street1,
                street2=street2,
                city=city,
                state=state,
                zipcode=zipcode,
                notes=notes,
                created_on=datetime.datetime.now(),
                created_by=request.authenticated_userid,
            )

            request.dbsession.add(family)
            request.dbsession.flush()

            request.session.flash('INFO: Added family')
            return HTTPFound(request.route_url('family.view', family_id=family.id))
        except Exception as e:
            raise e

    @view_config(route_name='family.update', request_method="POST")
    def family_update(self):
        request = self.request

        try:
            family_id = request.matchdict.get('family_id')

            last_name = request.parameters.get('last_name', None)
            married_on = request.parameters.get('married_on', None)
            married_on = datetime.datetime.strptime(married_on, '%m/%d/%Y') if married_on is not None else None
            street1 = request.parameters.get('street1', None)
            street2 = request.parameters.get('street2', None)
            city = request.parameters.get('city', None)
            state = request.parameters.get('state', None)
            zipcode = request.parameters.get('zipcode', None)
            photo = request.parameters.get('photo', None)
            notes = request.parameters.get('notes', None)
            active = request.parameters.get('active', None)
            active = True if active == 'on' else False

            family = request.dbsession.query(Family)\
                .filter(Family.id == family_id)\
                .one()

            family.last_name = last_name
            family.married_on = married_on
            family.street1 = street1
            family.street2 = street2
            family.city = city
            family.state = state
            family.zipcode = zipcode
            family.notes = notes
            family.active = active

            request.session.flash('INFO: Updated family')
            return HTTPFound(request.route_url('family.view', family_id=family.id))
        except exc.NoResultFound as e:
            raise HTTPNotFound
        except Exception as e:
            raise e

    @view_config(route_name='family.delete')
    def family_delete(self):
        request = self.request

        try:
            family_id = request.matchdict.get('family_id')

            query = request.dbsession.query(Family)\
                .filter(Family.id == family_id)

            family = query.one() # ensure non-404, will error out if not found

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
