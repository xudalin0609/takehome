import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    JSON_AS_ASCII = False
    ALLOWED_EXTENSIONS = set(['png', 'jpg'])
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = 'upload'
