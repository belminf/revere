"""Database bootstrap
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from .config import DATABASE_URL
from .app import app

engine = create_engine(DATABASE_URL, convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def get_db():
    return session, engine


@app.teardown_request
def teardown_request(exception):
    session.remove()
