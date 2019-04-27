from datasource.database_init import Base
from sqlalchemy.dialects.sqlite import UUID
from sqlalchemy import Column, Text, String


class Contact(Base):
    """ A contact """
    __tablename__ = "contact"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(Text, nullable=False)
    phone = Column(Text, nullable=True)
    address = Column(Text, nullable=True)
    email = Column(Text, nullable=False)
