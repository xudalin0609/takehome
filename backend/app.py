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


# def register_extensions(app):
#     db.init_app(app)
#     db_strategy_historical_data.init_app(app)


# def register_commands(app):
#     @app.cli.command()
#     @click.option('--drop', is_flag=True, help='Create after drop')
#     def initdb(drop):
#         if drop:
#             click.confirm(
#                 'This operation will delete the database, do you want ti continue?', abort=True)
#             db.drop_all()
#             click.echo('Drop tables')
#         db.create_all()
#         click.echo('Initialized database')


# def register_errors(app):
#     @app.errorhandler(400)
#     def bad_request(e):
#         return packing_return(code=400, message="error request")

#     @app.errorhandler(404)
#     def page_not_found(e):
#         return packing_return(code=404, message='not found')

#     @app.errorhandler(500)
#     def internal_server_error(e):
#         return packing_return(code=500, message='web server error')

#     @app.errorhandler(CustomFlaskErr)
#     def args_error(e):
#         return packing_return(code=10001, message='args error')

#     @app.errorhandler(NoSimilarErr)
#     def no_similar_error(e):
#         return packing_return(code=10002, message='no similar page')


if __name__ == "__main__":
    create_app().run()
