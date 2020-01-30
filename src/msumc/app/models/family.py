import datetime
 
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    Date,
    Boolean,
    ForeignKey,
)
 
from msumc.app.models.meta import Base
 
class Family(Base):
    __tablename__ = 'family'
    id = Column(Integer, primary_key=True, nullable=False)
    last_name = Column(String(128), nullable=False)
    married_on = Column(Date)
    street1 = Column(String(128))
    street2 = Column(String(128))
    city = Column(String(128))
    state = Column(String(128))
    zipcode = Column(String(128))
    photo_fp = Column(String(1000))
    active = Column(Boolean, nullable=False)

    notes = Column(String(1000))
    created_on = Column(DateTime, nullable=False)
    created_by = Column(String(128), nullable=False)
