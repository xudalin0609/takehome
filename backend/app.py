import os
import importlib

from flask import Flask
from flask_restful import Api


from settings import Config, ACTIVE_API
from blueprints.index import Index


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(Config)

    api = Api(app)
    register_api(api)
    print(app.url_map)
    return app


def register_api(api):
    api.add_resource(Index, '/', '/index')
    for path, endpoint in ACTIVE_API.values():
        ret, cls_name = path.rsplit(".", maxsplit=1)
        moudle = importlib.import_module(ret)
        clss = getattr(moudle, cls_name)
        api.add_resource(clss, *endpoint)


if __name__ == "__main__":
    create_app().run()
