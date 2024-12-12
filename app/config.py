import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Usar directamente la URL de conexión de MySQL que proporciona Railway
    SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_URL', 'mysql://root:password@localhost/railway')
    
    # Si tienes la URL pero necesitas ajustarla para SQLAlchemy
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("mysql://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("mysql://", "mysql+mysqldb://", 1)
    
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
