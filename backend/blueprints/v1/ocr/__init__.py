from flask import request, current_app
from flask_restful import Resource
from werkzeug.utils import secure_filename

from blueprints.v1.ocr.ocr_letters import img_ocr
from common.utils import field_struct_decorator
from models import OcrMessage
from common.extensions import db


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower(
           ) in current_app.config["ALLOWED_EXTENSIONS"]


class Ocr(Resource):

    def post(self):
        try:
            f = request.files['file']
        except Exception:
            return field_struct_decorator(code=10001, errmsg="Please upload file by parameter file")
        if f and allowed_file(f.filename):
            file_name = secure_filename(f.filename)
            try:
                msg = img_ocr(f)

            except Exception as e:
                print(e)
                return field_struct_decorator(code=10001, errmsg="Can't parse file as image")
            try:
                insert_field = OcrMessage(file_name=file_name, file_content=str(msg),
                                          from_ip=request.remote_addr)
                db.session.add(insert_field)
                db.session.commit()
            except Exception as e:
                print(f'InsertErr: {e}')
            return field_struct_decorator(content=msg)
        else:
            return field_struct_decorator(code=10001, errmsg="Can't parse file as image")

    def get(self):
        ocr_message_id = request.args.get('ocr_message_id', default=None)
        limit = request.args.get('limit', default=10, type=int)
        limit = min(limit, 200)
        if ocr_message_id is None:
            response_content = OcrMessage.query.limit(limit).all()
        else:
            response_content = OcrMessage.query.filter_by(ocr_message_id=ocr_message_id).all()

        if len(response_content) == 0:
            return field_struct_decorator(content=[])
        else:
            return field_struct_decorator(
                content={_.ocr_message_id: _.file_content
                         for _ in response_content})
