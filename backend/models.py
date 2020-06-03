import uuid

from common.extensions import db


def generate_uuid(table_name):
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, table_name)).replace("-", "")


class OcrMessage(db.Model):
    __tablename__ = 'ocr_message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ocr_message_id = db.Column(
        db.String(32), unique=True, default=generate_uuid(__tablename__))
    file_name = db.Column(db.String(80), unique=False)
    file_content = db.Column(db.Text, unique=False)
    from_ip = db.Column(db.String(40), unique=False)

    def __repr__(self):
        return '<User %r>' % self.username
