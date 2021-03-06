import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfiguration(object):
    DEBUG = False
    TESTING = False

    ADMINS = frozenset(['youremail@yourdomain.com'])
    SECRET_KEY = 'SecretKeyForSessionSigning'

    THREADS_PER_PAGE = 8

    DATABASE = 'app.db'
    DATABASE_PATH = os.path.join(basedir, DATABASE)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SECURITY_PASSWORD_SALT = 'SuPeRsEcReTsAlT'
    SECURITY_POST_LOGIN_VIEW = '/LatestGames'
    SECURITY_CHANGEABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_TRACKABLE = True

    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
    SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = False

    MAIL_SUPPRESS_SEND = True


class TestConfiguration(BaseConfiguration):
    TESTING = True

    DATABASE = 'tests.db'
    DATABASE_PATH = os.path.join(basedir, DATABASE)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # + DATABASE_PATH


class DebugConfiguration(BaseConfiguration):
    DEBUG = True
