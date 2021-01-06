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
from msumc.app.models.household import Household
from msumc.app.models.person import Person

@view_defaults(permission='view_directory')
class HouseholdViews:
    def __init__(self, request):
        self.request = request
        self.image_base_dir = f'{os.getcwd()}/msumc/app/static/img/household/'

        household_id = request.matchdict.get('household_id')

        married_on = request.parameters.get('married_on', None)
        self.last_name = request.parameters.get('last_name', None)
        self.married_on = datetime.datetime.strptime(married_on, '%m/%d/%Y') if married_on is not None else None
        self.street1 = request.parameters.get('street1', None)
        self.street2 = request.parameters.get('street2', None)
        self.city = request.parameters.get('city', None)
        self.state = request.parameters.get('state', None)
        self.zipcode = request.parameters.get('zipcode', None)
        self.notes = request.parameters.get('notes', None)
        self.photo = request.parameters.get('photo', b'')

        self.photo_fp = None
        if self.photo != b'':
            self.photo_fp = file.write_file(self.image_base_dir, self.photo)

        self.household = None
        if household_id:
            try:
                self.household = request.dbsession.query(Household)\
                    .filter(Household.id == household_id)\
                    .one()
            except exc.NoResultFound as e:
                raise HTTPNotFound

    @view_config(route_name='household.index', renderer='../templates/household/index.jinja2')
    def household_index(self):
        request = self.request

        try:
            households = request.dbsession.query(Household)\
                .order_by(Household.last_name)\
                .all()

            household_count = request.dbsession.query(Household.id, func.count(Person.id))\
                .select_from(Household)\
                .join(Person, Household.id == Person.household_id)\
                .group_by(Household.last_name)\
                .all()

            household_count = { household_id: count for household_id, count in household_count }

            return {
                'households': households,
                'household_count': household_count,
            }
        except Exception as e:
            request.session.flash(f"ERROR: {e}")

            return { }

    @view_config(route_name='household.view', renderer='../templates/household/view.jinja2')
    def household_view(self):
        request = self.request

        try:
            household_id = request.matchdict.get('household_id')

            household = request.dbsession.query(Household)\
                .filter(Household.id == household_id)\
                .one()

            people = request.dbsession.query(Person)\
                .filter(Person.household_id == household_id)\
                .order_by(Person.first_name)\
                .all()

            return {
                'household': household,
                'people': people,
            }
        except exc.NoResultFound as e:
            raise HTTPNotFound

    @view_config(route_name='household.add', renderer='../templates/household/add.jinja2', permission='administrate')
    def household_add_GET(self):
        request = self.request

        return {
        }

    @view_config(route_name='household.add', request_method="POST", permission='administrate')
    def household_add_POST(self):
        request = self.request

        household = Household(
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

        request.dbsession.add(household)
        request.dbsession.flush()

        request.session.flash('INFO: Added household')
        return HTTPFound(request.route_url('household.view', household_id=household.id))

    @view_config(route_name='household.update', request_method="POST", permission='administrate')
    def household_update(self):
        request = self.request

        self.household.last_name = self.last_name
        self.household.married_on = self.married_on
        self.household.street1 = self.street1
        self.household.street2 = self.street2
        self.household.city = self.city
        self.household.state = self.state
        self.household.zipcode = self.zipcode
        self.household.notes = self.notes

        if self.photo != b'':
            file.remove_file(self.household.photo_fp) # remove the old file from the system
            photo_fp = file.write_file(self.image_base_dir, self.photo) # add the new file to the system

            self.household.photo_fp = photo_fp

        request.session.flash('INFO: Updated household')
        return HTTPFound(request.route_url('household.view', household_id=self.household.id))

    @view_config(route_name='household.delete', permission='administrate')
    def household_delete(self):
        request = self.request

        try:
            household_id = request.matchdict.get('household_id')

            query = request.dbsession.query(Household)\
                .filter(Household.id == household_id)

            household = query.one() # ensure non-404, will error out if not found

            file.remove_file(household.photo_fp) # remove the old file from the system

            # Delete people
            request.dbsession.query(Person)\
                .filter(Person.household_id == household.id)\
                .delete()

            # Delete Household
            query.delete()

            request.session.flash('INFO: Deleted household')
            return HTTPFound(request.route_url('household.index'))
        except exc.NoResultFound as e:
            raise HTTPNotFound
        except Exception as e:
            raise e
