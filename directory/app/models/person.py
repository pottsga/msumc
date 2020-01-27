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
 
from directory.app.models.meta import Base
 
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, nullable=False)
    family_id = Column(Integer, ForeignKey('family.id'))
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    phone_number = Column(String(128))
    email = Column(String(128))
    gender = Column(Enum('M', 'F'))
    is_child = Column(Boolean, nullable=False, default=False)
    birthday = Column(Date)

    notes = Column(String(1000))
    created_on = Column(DateTime, nullable=False)
    created_by = Column(String(128), nullable=False)
