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
 
class PageHit(Base):
    __tablename__ = 'page_hit'
    id = Column(Integer, primary_key=True, nullable=False)
    page_id = Column(Integer, ForeignKey('page.id'))
    ip_address = Column(String(128))
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.now())
