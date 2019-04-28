from datasource.database_init import Base
from sqlalchemy import Column, Text, String


class Contact(Base):
    """ A contact """
    __tablename__ = "contacts"
    id = Column(String(100), primary_key=True)
    name = Column(Text, nullable=False)
    phone = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    email = Column(String(256), nullable=False)

