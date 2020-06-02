from settings import ACTIVE_API

from flask import jsonify
from flask_restful import Resource


class Index(Resource):

    def get(self):
        def to_index():
            return {k: v[1] for k, v in ACTIVE_API.items()}
        return jsonify(to_index())
