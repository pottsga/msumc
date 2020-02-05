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
 
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, nullable=False)
    family_id = Column(Integer, ForeignKey('family.id'))
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    phone_number = Column(String(128))
    email = Column(String(128))
    gender = Column(Enum('M', 'F'))
    birthday = Column(Date)
    is_child = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, nullable=False)

    notes = Column(String(1000))
    created_on = Column(DateTime, nullable=False)
    created_by = Column(String(128), nullable=False)
