class Config(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    DB_NAME = "contactsDB"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"
    SQLALCHEMY_DATABASE_URI =f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}'
    # 'mysql+pymysql://DB_USERNAME:DB_PASSWORD@localhost/DB_NAME' 
    IMAGE_UPLOADS = "E:\python\contactApp\app\static\static\img"

    SESSION_COOKIE_SECURE = False

    BCRYPT_LOG_ROUNDS = 12
