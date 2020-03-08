import os
import sys
import transaction
import datetime

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from msumc.security import hash_password

from msumc.app.models import (
    get_engine,
    get_session_factory,
    get_tm_session
)

from msumc.app.models import Base, User, Page, Household, Person

from msumc.initial_html import pages

def usage(argv):
    cmd = os.path.basename(argv[0])
    print(f"""
        Usage: {cmd} <config_uri> [var=value]
        (example: {cmd} development.ini)
    """)
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        u = User(
            email='pottsga@gmail.com',
            password=hash_password('asdf'),
            first_name='Greg',
            last_name='Potts',
            groups=['group:admins'],
            created_on=datetime.datetime.now(),
            created_by='SYSTEM',
            last_signed_in_on=datetime.datetime.now(),
        )
        dbsession.add(u)

        h = Household(
            last_name='Potts',
            married_on=datetime.date(year=2019, month=10, day=5),
            street1='720 Laurel Ave. E.',
            city='Greenwood',
            state='SC',
            zipcode='29649',
            created_on=datetime.datetime.now(),
            created_by='SYSTEM',
        )
        dbsession.add(h)
        dbsession.flush()

        p = Person(
            household_id=h.id,
            first_name='Greg',
            last_name='Potts',
            email='potts.ga@gmail.com',
            created_on=datetime.datetime.now(),
            created_by='SYSTEM',
        )
        dbsession.add(p)

        dbsession.add_all(pages)
