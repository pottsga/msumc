import datetime
 
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    Date,
    Boolean,
    ForeignKey,
    Enum,
)
 
from msumc.app.models.meta import Base
 
class EmailVerification(Base):
    __tablename__ = 'email_verification'
    id = Column(Integer, primary_key=True, nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    verification_id = Column(String(10000), nullable=False)
    expires_on = Column(DateTime, nullable=False)
    created_on = Column(DateTime, nullable=False)
