import unittest
import transaction

import logging
log = logging.getLogger(__name__)

from msumc.app.models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    Base,
    Page,
)

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        from webtest import TestApp
        from msumc import main
        from msumc.initial_html import pages
        from pyramid.paster import get_appsettings

        config_uri = 'testing.ini'
        settings = get_appsettings(config_uri)

        app = main({}, **settings)

        engine = get_engine(settings)
        Base.metadata.create_all(engine)

        self.session_factory = get_session_factory(engine)

        log.info('...')

        with transaction.manager:
            dbsession = get_tm_session(self.session_factory, transaction.manager)

            pages = dbsession.query(Page).all()

            log.info(pages)

        # settings = get_appsettings('development.ini', name='main')
        # app = main({}, **settings)

        # engine = create_engine('sqlite://')
        # Base.metadata.create_all(engine)

        # Session = sessionmaker(bind=engine)
        # self.session = Session()
        # print(Session())
        # with transaction.manager:
        #     self.session.add_all(pages)

        self.testapp = TestApp(app)

    def test_index(self):
        res = self.testapp.get('/', status=302).follow()
        assert b'Main Street' in res.body

    def test_contact_us(self):
        res = self.testapp.get('/contact_us', status=200)
        assert b'Contact Us' in res.body
    
    # def test_pages(self):
    #     from msumc.app.models import Page


    #     with transaction.manager:
    #         dbsession = get_tm_session(self.session_factory, transaction.manager)

    #         # pages = dbsession.query(Page).all()

