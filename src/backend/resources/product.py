import json
from flask_restful import Resource, request
from backend.models import Product
from backend.models.database import db
from backend.schema import ProductSchema
from backend.utils.query_helpers import careful_query


class ProductResource(Resource):

    def get(self):
        result = _query_all()
        return result, 200

    def post(self):
        payload = request.json
        if not isinstance(payload, dict):
            try:
                payload = json.loads(payload)
            except Exception as e:
                return f'Failed to parse payload: {e}', 400

        new_entry = Product(**payload)
        db.session.add(new_entry)
        db.session.commit()

        return payload, 201


@careful_query
def _query_all():
    items = Product.query.all()
    return ProductSchema(many=True).dump(items)
