from sqlalchemy import Column, String, Integer
from revere.database import get_base


Base = get_base()


class Subscriber(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    to_email = Column(String(256))
    cc_email = Column(String(512))
