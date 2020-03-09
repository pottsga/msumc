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
    Text,
)
 
from msumc.app.models.meta import Base
 
class Page(Base):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True, nullable=False)

    path = Column(String(128), nullable=False, unique=True)
    title = Column(String(128), nullable=False)
    body = Column(Text(1000000), nullable=False)

    updated_on = Column(DateTime)
    updated_by = Column(String(128))
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.now())
    created_by = Column(String(128), nullable=False)
