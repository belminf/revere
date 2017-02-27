from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from flask_restful import fields
from revere.database import get_db, get_base
from revere.models.subscribers import Subscriber
from revere.models.announcements import Announcement


db_session, db_engine = get_db()
Base = get_base()


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


TagFields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
}


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    description = Column(String(256))
    subscribers = relationship('Subscriber', secondary=tag_subscribers_table, backref='tags')
    announcements = relationship('Announcement', secondary=tag_announcements_table, backref='tags')

