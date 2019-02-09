from os import path


basedir = path.abspath(path.dirname(__file__))

class Testing:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, '..', 'test.db')


class Production:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, '..', 'app.db')
