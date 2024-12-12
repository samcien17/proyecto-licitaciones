import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:toudUHgpZvFYzDkhKIbEnUrotwYopNhY@autorack.proxy.rlwy.net:16919/railway"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
        'pool_timeout': 900,
        'pool_size': 10,
        'max_overflow': 5,
        'connect_args': {
            'connect_timeout': 60
        }
    }
