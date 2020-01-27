from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.session import SignedCookieSessionFactory
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .resources import Root
from .security import groupfinder
from .request_methods import parameters


def main(global_config, **settings):
    config = Configurator(
        settings=settings, 
        root_factory=Root,
    )

    config.include('pyramid_jinja2')
    config.include('.routes')
    config.include('.app.models')

    config.add_request_method(parameters, reify=True)

    # Session factory
    session_secret = settings['session.secret']
    sess_factory = SignedCookieSessionFactory(
        session_secret,
        reissue_time=1,
        max_age=28800
    )
    config.set_session_factory(sess_factory)

    # Security Policies
    auth_secret = settings['auth.secret']
    authn_policy = AuthTktAuthenticationPolicy(
        auth_secret,
        callback=groupfinder,
        hashalg='sha512',
        reissue_time=1,
        max_age=28800
    )

    authz_policy = ACLAuthorizationPolicy()

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.scan()

    return config.make_wsgi_app()
