#!/usr/bin/env python3
import os
import sys
from flask import Flask
from utils.server_logger import logger


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)

    err = _initialize_db(app)
    if err:
        logger.error(f'Database init failed: {err}')
        sys.exit(1)

    return app


def _initialize_db(app):
    try:
        from backend.models.database import db
        db.init_app(app)

        with app.app_context():
            db.create_all()
            db.session.commit()
    except Exception as e:
        return e


if __name__ == '__main__':
    logger.info(f'Starting server...')

    config = {}
    config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////tmp/database.db'

    flask_app = create_app(config)
    flask_app.run(host=os.getenv('APP_HOST', '127.0.0.1'),
                  port=os.getenv('APP_PORT', 5005))
