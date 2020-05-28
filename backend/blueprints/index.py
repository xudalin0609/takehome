from flask import Blueprint, jsonify

bp_index = Blueprint('bp_index', __name__)


@bp_index.route('/', methods=['GET'])
def index():
    return jsonify({'code': 200})
