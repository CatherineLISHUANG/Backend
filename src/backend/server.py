#!/usr/bin/env python3
import os
import sys
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from backend.resources import CustomerResource
from backend.resources import FreightResource
from backend.utils.server_logger import logger


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)

    err = _initialize_db(app)
    if err:
        logger.error(f'Database init failed: {err}')
        sys.exit(1)

    # Setup CORS
    allowed_origins = [
        'http://127.0.0.1:5010'
    ]
    if os.getenv('FRONTEND_URL'):
        allowed_origins.extend(os.getenv('FRONTEND_URL'))
    CORS(app, resources={
        r"/api/v1/customer": {"origins": allowed_origins},
    })

    # Register api resources
    api = Api(app)
    api.add_resource(CustomerResource, '/api/v1/customer')
    api.add_resource(FreightResource, '/api/v1/freight')

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
