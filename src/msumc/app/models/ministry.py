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
 
class Ministry(Base):
    __tablename__ = 'ministry'
    id = Column(Integer, primary_key=True, nullable=False)
    family_id = Column(Integer, ForeignKey('family.id'))
    title = Column(String(256), nullable=False)
    description = Column(String(12800), nullable=False)

    started_on = Column(DateTime)
    active = Column(Boolean, nullable=False)

    notes = Column(String(1000))
    created_on = Column(DateTime, nullable=False)
    created_by = Column(String(128), nullable=False)
