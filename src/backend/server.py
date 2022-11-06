#!/usr/bin/env python3
import os
import sys
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from backend.resources import CustomerResource
from backend.resources import CityResource
from backend.resources import FreightResource
from backend.resources import OrderResource
from backend.resources import ProductResource
from backend.resources import GroupedResource
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
    CORS(app)
    # Register api resources
    api = Api(app)

    list_of_resources = [
        CustomerResource,
        CityResource,
        FreightResource,
        OrderResource,
        ProductResource,
        GroupedResource,
    ]

    list_of_resource_and_endpoints = [
        (res, f'/api/v1/{res.__name__.replace("Resource", "").lower()}') for
        res in list_of_resources
    ]

    for res, ep in list_of_resource_and_endpoints:
        api.add_resource(res, ep)


    @app.route('/')
    def home():
        app_host = 'http://127.0.0.1:5005'
        anchors = [
            f'<a href="{app_host}{ep}">{ep}</a>' for _, ep
            in list_of_resource_and_endpoints
        ]
        return '<br>'.join(anchors)

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
