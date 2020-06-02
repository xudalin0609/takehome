from flask import request, current_app
from flask_restful import Resource
from werkzeug.utils import secure_filename

from blueprints.v1.ocr.ocr_letters import img_ocr
from common.utils import field_struct_decorator


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower(
           ) in current_app.config["ALLOWED_EXTENSIONS"]


class Ocr(Resource):

    def post(self):
        try:
            f = request.files['file']
        except Exception:
            return field_struct_decorator(code=404, errmsg="Please upload file by parameter file")
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            try:
                msg = img_ocr(f)
            except Exception:
                return field_struct_decorator(code=1001, errmsg="Can't parse file as image")
            return field_struct_decorator(data=msg)
        else:
            return field_struct_decorator(code=1001, errmsg="Can't parse file as image")
