from pyramid.httpexceptions import HTTPNotFound
from pyramid.security import Allow, Everyone
 
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)
 
import datetime
 
from msumc.app.models.columns import ArrayType
from msumc.app.models.meta import Base
 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(120), unique=True)
    password = Column(String(120), nullable=False)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    groups = Column(ArrayType, nullable=False)
    created_on = Column(DateTime, nullable=False)
    last_signed_in_on = Column(DateTime, nullable=False)
 
def user_factory(request):
    user_id = request.matchdict.get('id')
    if user_id is None:
        # Return the class
        return User
    user_id_int = int(user_id)
    user = request.dbsession.query(User).filter_by(id=user_id_int).first()
    if not user:
        raise HTTPNotFound()
    return user
