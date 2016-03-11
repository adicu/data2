"""
Collects settings from the environment and adds them to the app configuration.

Flask specific settings will be set here and we can store additional settings
in the config object as well.
"""

from os import environ, pardir
from os.path import join, abspath, dirname
from sys import exit

try:
    # flask settings
    HOST = environ['HOST']
    PORT = environ['PORT']
    SECRET_KEY = environ['SECRET_KEY']
    DEBUG = environ['DEBUG'] == 'TRUE'

    BASEDIR = abspath(join(dirname(__file__), pardir))

    # DB Settings
    SQLALCHEMY_DATABASE_URI = "postgresql://%s:%s@%s:%s/%s" % (
        environ['DB_USER'],
        environ['DB_PASS'],
        environ['DB_HOST'],
        environ['DB_PORT'],
        environ['DB_NAME']
    )

except KeyError as e:
    """ Throw an error if a setting is missing """
    exit("Some of your settings aren't in the environment."
         "You probably need to run:"
         "\n\tsource config/<your settings file>\n")
