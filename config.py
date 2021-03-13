class Config(object):
    pass

class ProdConfig(Config):
    SECRET_KEY = 'Your secret key'

class DevConfig(Config):
    debug=True
    SECRET_KEY = 'The other secret key'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost:3306/flask1"
