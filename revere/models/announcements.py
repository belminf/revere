from sqlalchemy import Column, String, Integer, DateTime, Boolean
from revere.database import get_base


Base = get_base()


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
