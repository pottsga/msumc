import bcrypt

from sqlalchemy.orm.exc import NoResultFound
from msumc.app.models.user import User

def hash_password(pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    return pwhash.decode('utf8')

def check_password(pw, hashed_pw):
    matches = bcrypt.checkpw(pw.encode('utf8'), hashed_pw.encode('utf8'))
    return matches

def groupfinder(email, request):
    groups = []
    try:
        user = request.dbsession.query(User)\
            .filter(User.email == email)\
            .one()
    except NoResultFound:
        pass
    else:
        groups = user.groups
    return groups
