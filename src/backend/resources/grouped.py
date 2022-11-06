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
            if len(filtered) > 0:
                total_score = sum([_calc_sth(o) for o in filtered])
                avg_score = total_score / len(filtered)
                grouped.append({
                    'departure_city_name': city,
                    'total_score': total_score,
                    'avg_score': avg_score,
                    'items': filtered
                })
            else:
                grouped.append({
                    'departure_city_name': city,
                    'total_score': 0,
                    'avg_score': 0,
                    'items': []
                })

        grouped.sort(key=lambda k: k['total_score'], reverse=True)
        return grouped, 200

@careful_query
def _query_all():
    items = Freight.query.all()
    return FreightSchema(many=True).dump(items)

def _calc_sth(freight):
    distance = freight.get('pre_calc_distance')
    weight = freight.get('pre_calc_weight')
    volume = freight.get('pre_calc_volume')
    price = freight.get('pre_calc_price')
    if price > 0 and distance and weight and volume:
        return (0.1 * float(distance) + 0.15 * float(weight) + 0.12 * float(volume)) / float(price)
    return 10
