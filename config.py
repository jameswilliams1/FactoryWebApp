from os import path


basedir = path.abspath(path.dirname(__file__))

class Testing:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'# In-memory db for testing
    DEBUG = True


class Production:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, '..', 'db_prod.db')
