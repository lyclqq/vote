
import os
SECRET_KEY=os.urandom(24)


CKEDITOR_SERVE_LOCAL=True
CKEDITOR_HEIGHT=600
CKEDITOR_FILE_UPLOADER='upload'
CKEDITOR_ENABLE_CSRF=True
UPLOAD_FOLDER='static\\files\\'
SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Panda1@127.0.0.1:3306/vote?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS=True
