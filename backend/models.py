import uuid
import time

from common.extensions import db


def generate_uuid(table_name):
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, str(time.time()))).replace("-", "")


class OcrMessage(db.Model):
    __tablename__ = 'ocr_message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ocr_message_id = db.Column(
        db.String(32), unique=True, default=generate_uuid(__tablename__))
    file_name = db.Column(db.String(80), unique=False)
    file_content = db.Column(db.Text, unique=False)
    from_ip = db.Column(db.String(40), unique=False)

    def __repr__(self):
        return '<ocr_message_id %r>' % self.ocr_message_id
