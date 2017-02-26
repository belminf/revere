"""Configuraiton values

Should default to something sane.
"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///revere.db')
DEBUG = True
