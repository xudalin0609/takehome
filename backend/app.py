import os

from flask import Flask

from settings import Config
from blueprints.index import bp_index
from blueprints.v1 import bp_v1


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask(__name__)

    app.config.from_object(Config)
    register_blueprint(app)
    return app


def register_blueprint(app):
    app.register_blueprint(bp_index, url_prefix='/')
    app.register_blueprint(bp_v1, url_prefix='/api/v1')


if __name__ == "__main__":
    create_app().run()
