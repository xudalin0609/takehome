import os
import base64
import time

from flask import Blueprint, jsonify, request, current_app
from werkzeug.utils import secure_filename

bp_v1 = Blueprint('bp_v1', __name__)


@bp_v1.route('/', methods=['GET'])
def index():
    return jsonify({'code': 200, 'type': 'v1'})


@bp_v1.route('/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(basedir, current_app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['myfile']
    if f:
        fname = secure_filename(f.filename)
        print(fname)
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext  # 修改了上传的文件名
        print(file_dir) 
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录
        return jsonify({"code": 0, "errmsg": "上传成功",
                        "fileName": "/api/download/" + new_filename})
    else:
        return jsonify({"code": 1001, "errmsg": "上传失败"})
