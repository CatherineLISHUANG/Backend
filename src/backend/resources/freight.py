import json
from flask_restful import Resource, request
from backend.models import Freight
from backend.models.database import db
from backend.schema import FreightSchema
from backend.utils.query_helpers import careful_query


class FreightResource(Resource):

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

        new_entry = Freight(**payload)
        db.session.add(new_entry)
        db.session.commit()

        return payload, 201


@careful_query
def _query_all():
    items = Freight.query.all()
    return FreightSchema(many=True).dump(items)
