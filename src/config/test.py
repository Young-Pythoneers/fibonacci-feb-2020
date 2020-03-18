# noinspection PyUnresolvedReferences
from config.prod import *  # noqa

##############################
# Overwrite prod config values
##############################

SQLALCHEMY_DATABASE_URI = "sqlite://"  # Uses in-memory database
