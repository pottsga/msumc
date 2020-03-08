import datetime
import logging
import uuid
import smtplib

from email.mime.text import MIMEText

from pyramid.httpexceptions import HTTPBadRequest, HTTPFound
from pyramid.security import forget, remember
from pyramid.view import view_config
from sqlalchemy.orm import exc

from ..models import User, Person, EmailVerification
from msumc.app import functions
from msumc.security import check_password, hash_password

logger = logging.getLogger(__name__)

class AuthViews:
    def __init__(self, request):
        self.request = request
        self.VERIFICATION_TIMEOUT_HOURS = 2

    @view_config(route_name='auth.login', renderer='../templates/auth/login.jinja2', request_method="GET")
    def auth_login_GET(self):
        request = self.request

        return {
        }

    @view_config(route_name='auth.login', request_method="POST")
    def auth_login_POST(self):
        request = self.request

        email = request.params.get('email', None)
        password = request.params.get('password', None)

        try:
            user = request.dbsession.query(User)\
                .filter(User.email == email)\
                .one()

            password_matches = check_password(password, user.password)

            if not password_matches:
                raise ValueError('Password incorrect')

            user.last_signed_in_on = datetime.datetime.now()

            headers = remember(request, user.email)
            request.session.flash(f'INFO: Welcome, {user.email}')

            print(user.groups)

            if 'group:admins' in user.groups:
                return HTTPFound(request.route_url('admin.index'), headers=headers)
            elif 'group:members' in user.groups:
                return HTTPFound(request.route_url('directory.index'), headers=headers)

        except exc.NoResultFound as e:
            request.session.flash(f'ERROR: You do not have an account. Please make sure your email is correct.')
            return HTTPFound(request.route_url('auth.login'))
        except ValueError as e:
            error = str(e)

            if error == 'Password incorrect':
                request.session.flash(f'ERROR: Incorrect password.')
                return HTTPFound(request.route_url('auth.login'))

    @view_config(route_name='auth.logout', request_method="GET")
    def auth_logout(self):
        request = self.request
        headers = forget(request)

        return HTTPFound(request.route_url('index.index'), headers=headers)

    @view_config(route_name='auth.register', renderer='../templates/auth/register.jinja2', request_method="GET")
    def auth_register_GET(self):
        request = self.request

        return {
        }

    @view_config(route_name='auth.register', request_method="POST")
    def auth_register_POST(self):
        request = self.request

        email = request.params.get('email', None)

        try:
            person = request.dbsession.query(Person)\
                .filter(Person.email == email)\
                .one()

            if person.is_email_verified:
                request.session.flash('INFO: Email is already verified.')
                return HTTPFound(request.route_url('auth.login'))

            verification_id = uuid.uuid4().int
            
            ## Create a verification record
            verification_route = request.route_url('auth.verify', verification_id=verification_id)

            message = f'''
            <p>Please use the following link to verify your email address with the MSUMC system <a href="{verification_route}">Verify email</a>.</p>
            <p>This code expires in <code>{self.VERIFICATION_TIMEOUT_HOURS} hours</code>.</p>
            '''

            functions.email.send_email(email, 'Verification', message)

            email_verification = EmailVerification(
                person_id=person.id,
                verification_id=f'{verification_id}',
                expires_on=datetime.datetime.now() + datetime.timedelta(hours=self.VERIFICATION_TIMEOUT_HOURS),
                created_on=datetime.datetime.now(),
            )

            request.dbsession.add(email_verification)

            request.session.flash('INFO: If you have an email on file in our system, you should receive an email from our system shortly asking you to verify your account!')
        except exc.NoResultFound as e:
            request.session.flash('ERROR: No person found in our system with that email. Please contact the church office if you believe this is incorrect.')
        return HTTPFound(request.route_url('auth.register'))

    @view_config(route_name='auth.verify', renderer='../templates/auth/verify.jinja2', request_method="GET")
    def auth_verify_GET(self):
        request = self.request
        verification_id = request.matchdict.get('verification_id')

        try:
            email_verification = request.dbsession.query(EmailVerification)\
                .filter(
                    EmailVerification.verification_id == verification_id,
                    EmailVerification.expires_on >= datetime.datetime.now(),
                )\
                .one()

            return {
                'email_verification': email_verification,        
            }
        except exc.NoResultFound as e:
            request.session.flash('ERROR: Verification time limit timed out. Please try again later.')
            return HTTPFound(request.route_url('auth.register'))

    @view_config(route_name='auth.verify', request_method="POST")
    def auth_verify_POST(self):
        request = self.request
        verification_id = request.matchdict.get('verification_id')
        password = request.params.get('password')

        try:

            email_verification = request.dbsession.query(EmailVerification)\
                .filter(
                    EmailVerification.verification_id == verification_id,
                    EmailVerification.expires_on >= datetime.datetime.now(),
                )\
                .first()

            if not email_verification:
                request.session.flash('ERROR: Could not verify your request. Please try again later.')
                return HTTPFound(request.route_url('auth.forgot_password'))

            person = request.dbsession.query(Person)\
                .filter(Person.id == email_verification.person_id)\
                .first()

            person.is_email_verified = True

            u = User(
                email=person.email,
                password=hash_password(password),
                first_name=person.first_name,
                last_name=person.last_name,
                groups=['group:members'],
                created_on=datetime.datetime.now(),
                created_by='SYSTEM',
            )

            request.dbsession.add(u)
            request.session.flash("SUCCESS: Verified email successfully")
            return HTTPFound(request.route_url('auth.login'))
        except Exception as e:
            request.session.flash('ERROR: Could not verify your account. Please try again later.')
            return HTTPFound(request.route_url('auth.register'))

    @view_config(route_name='auth.forgot_password', renderer='../templates/auth/forgot_password.jinja2', request_method="GET")
    def auth_forgot_password_GET(self):
        request = self.request
        return {
        }

    @view_config(route_name='auth.forgot_password', request_method="POST")
    def auth_forgot_password_POST(self):
        request = self.request
        email = request.params.get('email')

        try:
            person = request.dbsession.query(Person)\
                .filter(Person.email == email)\
                .one()

            if not person.is_email_verified:
                request.session.flash('ERROR: Email is not already verified. Please register your email first.')
                return HTTPFound(request.route_url('auth.register'))

            verification_id = uuid.uuid4().int
            
            ## Create a verification record
            reset_route = request.route_url('auth.reset_password', verification_id=verification_id)
            message = f'''
            <p>Please use the following link to reset your password in the MSUMS system <a href="{reset_route}">Reset Password</a>.</p>
            <p>This code expires in <code>{self.VERIFICATION_TIMEOUT_HOURS} hours</code>.</p>
            '''

            functions.email.send_email(email, 'Reset Password', message)

            email_verification = EmailVerification(
                person_id=person.id,
                verification_id=f'{verification_id}',
                expires_on=datetime.datetime.now() + datetime.timedelta(hours=self.VERIFICATION_TIMEOUT_HOURS),
                created_on=datetime.datetime.now(),
            )

            request.dbsession.add(email_verification)

            request.session.flash('INFO: Sent an email to the email on file. Please check your email.')
        except Exception as e:
            request.session.flash('ERROR: Could not reset your password. Please try again later.')
        return HTTPFound(request.route_url('auth.forgot_password'))

    @view_config(route_name='auth.reset_password', renderer='../templates/auth/reset_password.jinja2', request_method="GET")
    def auth_reset_password_GET(self):
        request = self.request
        verification_id = request.matchdict.get('verification_id')

        try:
            email_verification = request.dbsession.query(EmailVerification)\
                .filter(
                    EmailVerification.verification_id == verification_id,
                    EmailVerification.expires_on >= datetime.datetime.now(),
                )\
                .one()

            return {
                'email_verification': email_verification,        
            }
        except exc.NoResultFound as e:
            request.session.flash('ERROR: Verification time limit timed out. Please try again later.')
            return HTTPFound(request.route_url('auth.register'))

    @view_config(route_name='auth.reset_password', request_method="POST")
    def auth_reset_password_POST(self):
        request = self.request
        verification_id = request.matchdict.get('verification_id')
        password = request.params.get('password')

        try:
            email_verification = request.dbsession.query(EmailVerification)\
                .filter(
                    EmailVerification.verification_id == verification_id,
                    EmailVerification.expires_on >= datetime.datetime.now(),
                )\
                .first()

            if not email_verification:
                request.session.flash('ERROR: Could not verify your request. Please try again later.')
                return HTTPFound(request.route_url('auth.forgot_password'))

            person = request.dbsession.query(Person)\
                .filter(Person.id == email_verification.person_id)\
                .first()

            user = request.dbsession.query(User)\
                .filter(User.email == person.email)\
                .first()

            user.password = hash_password(password)

            request.session.flash("SUCCESS: Reset your password.")
            return HTTPFound(request.route_url('auth.login'))
        except Exception as e:
            request.session.flash('ERROR: Could not reset your account. Please try again later.')
            return HTTPFound(request.route_url('auth.forgot_password'))
