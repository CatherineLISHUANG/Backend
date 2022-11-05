import json
from flask_restful import Resource, request
from backend.models import Customer
from backend.models.database import db
from backend.schema import CustomerSchema
from backend.utils.query_helpers import careful_query
from backend.utils.query_helpers import dump_results


class CustomerResource(Resource):

    def get(self):
        result = _query_all()
        return dump_results(result), 200

    def post(self):
        payload = request.json
        if not isinstance(payload, dict):
            try:
                payload = json.loads(payload)
            except Exception as e:
                return f'Failed to parse payload: {e}', 400

        new_customer = Customer(**payload)
        db.session.add(new_customer)
        db.session.commit()

        return payload, 201


@careful_query
def _query_all():
    items = Customer.query.all()
    return CustomerSchema(many=True).dump(items)
