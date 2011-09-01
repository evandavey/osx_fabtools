"""
Idempotent API for managing PostgreSQL users and databases
"""
from fabtools.postgres import *


def user(name, passwd):
    """
    I can haz PostgreSQL user
    """
    if not user_exists(name):
        create_user(name, passwd)
        sudo('''psql -c "CREATE USER %(name)s WITH PASSWORD '%(passwd)s';"''' % locals(), user='postgres')


def database(name, owner):
    """
    I can haz PostgreSQL database
    """
    if not database_exists(name):
        create_database(name, owner)