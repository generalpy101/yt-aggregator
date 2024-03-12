import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class DevConfig(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")

# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.db")
#     ELASTICSEARCH_URL = None