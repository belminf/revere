"""Database bootstrap
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from revere.config import DATABASE_URL
from revere import app

engine = create_engine(DATABASE_URL, convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = session.query_property()


def get_db():
    return session, engine


def get_base():
    return Base


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@app.teardown_request
def teardown_request(exception):
    session.remove()
