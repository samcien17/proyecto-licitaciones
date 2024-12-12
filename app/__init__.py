from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
import time
import logging

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import api
    app.register_blueprint(api)

    with app.app_context():
        max_retries = 5
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                db.create_all()
                break
            except Exception as e:
                retry_count += 1
                if retry_count == max_retries:
                    app.logger.error(f"Failed to connect to database after {max_retries} attempts")
                    raise e
                app.logger.warning(f"Database connection attempt {retry_count} failed, retrying in 5 seconds...")
                time.sleep(5)

    return app