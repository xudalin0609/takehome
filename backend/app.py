import os
import importlib
import click

from flask import Flask
from flask_restful import Api

from common.extensions import db
from common.utils import field_struct_decorator
from settings import config, ACTIVE_API
from blueprints.index import Index


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    api = Api(app)
    register_commands(app)
    register_extensions(app)
    register_api(api)
    register_errors(app)
    return app


def register_api(api):
    api.add_resource(Index, '/', '/index')
    for path, endpoint in ACTIVE_API.values():
        ret, cls_name = path.rsplit(".", maxsplit=1)
        moudle = importlib.import_module(ret)
        clss = getattr(moudle, cls_name)
        api.add_resource(clss, *endpoint)


def register_extensions(app):
    db.init_app(app)


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm(
                'This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return field_struct_decorator(code=10001, message="Bad reuquest")

    @app.errorhandler(404)
    def error_request(e):
        return field_struct_decorator(code=10002, message="Not found")

    @app.errorhandler(500)
    def internal_server_error(e):
        return field_struct_decorator(code=20001, errmsg='Web server error')


if __name__ == "__main__":
    create_app().run()
