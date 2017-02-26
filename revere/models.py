"""Models declerations
"""

from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import get_db


db_session, db_engine = get_db()

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.drop_all(bind=db_engine)
    Base.metadata.create_all(bind=db_engine)


tag_subscribers_table = Table(
    'tag_subscribers',
    Base.metadata,
    Column('tag_id', Integer, ForeignKey('tags.id')),
    Column('subscriber_id', Integer, ForeignKey('subscribers.id'))
)

tag_announcements_table = Table(
    'tag_announcements',
    Base.metadata,
    Column('tag_id', Integer, ForeignKey('tags.id')),
    Column('announcement_id', Integer, ForeignKey('announcements.id'))
)


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    description = Column(String(256))
    subscribers = relationship('Subscriber', secondary=tag_subscribers_table, backref='tags')
    announcements = relationship('Announcement', secondary=tag_announcements_table, backref='tags')


class Subscriber(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    to_email = Column(String(256))
    cc_email = Column(String(512))


class Announcement(Base):
    __tablename__ = 'announcements'

    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    description = Column(String(1024))
    external_url = Column(String(512))
    extranl_email = Column(String(256))
    announce_date = Column(DateTime())
    start_date = Column(DateTime())
    announced = Column(Boolean(), default=False)
