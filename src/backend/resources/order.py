import json
from flask_restful import Resource, request
from backend.models import Order
from backend.models.database import db
from backend.schema import OrderSchema
from backend.utils.query_helpers import careful_query
from backend.utils.query_helpers import dump_results


class OrderResource(Resource):

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


        if payload.get('date'):
            import datetime
            as_date = datetime.datetime.strptime(payload.get('date'), "%Y-%m-%d")
            payload['date'] = as_date

        new_entry = Order(**payload)
        db.session.add(new_entry)
        db.session.commit()

        return OrderSchema().dump(Order.query.get(new_entry.id)), 201


@careful_query
def _query_all():
    items = Order.query.all()
    return OrderSchema(many=True).dump(items)
