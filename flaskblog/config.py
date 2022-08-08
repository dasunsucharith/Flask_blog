import os

class Config:
    SECRET_KEY = '843eaa1491c7a4130988d7c3ee4a9f4c'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')