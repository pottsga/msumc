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
 
class Upload(Base):
    __tablename__ = 'upload'
    id = Column(Integer, primary_key=True, nullable=False)
    fp = Column(String(1000))
    note = Column(String(9999))
    created_on = Column(DateTime, nullable=False)
    created_by = Column(String(128), nullable=False)
