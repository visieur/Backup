import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY ='fguob87fy3o784ryb8o7rbq3orqr478orbg4r78obo3r'
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'users.db')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

