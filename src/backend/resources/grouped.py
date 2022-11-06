import json
from flask_restful import Resource, request
from backend.models import Freight
from backend.models.database import db
from backend.schema import FreightSchema
from backend.utils.query_helpers import careful_query
from backend.utils.query_helpers import dump_results


class GroupedResource(Resource):

    def get(self):
        result = _query_all()
        all_cities = set(o['departure_city']['name'] for o in result)

        grouped = []
        for city in all_cities:
            filtered = [o for o in result if o['departure_city']['name'] == city]
            grouped.append({
                'departure_city_name': city,
                'items': filtered
            })
        return grouped, 200

@careful_query
def _query_all():
    items = Freight.query.all()
    return FreightSchema(many=True).dump(items)
