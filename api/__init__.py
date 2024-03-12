import os
import time

from flask import Flask
from flask_cors import CORS
from logging import Logger

from db import db

from werkzeug.exceptions import BadRequest, Unauthorized, InternalServerError

cors = CORS()

logger = Logger(__name__)


def create_app(config_class=None):
    app = Flask(__name__)
    if config_class:
        app.config.from_object(config_class)
    db.init_app(app)
    cors.init_app(app)

    return app
