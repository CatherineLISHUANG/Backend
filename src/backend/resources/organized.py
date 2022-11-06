import json
from flask_restful import Resource, request
from backend.models import Product
from backend.models.database import db
from backend.schema import ProductSchema
from backend.utils.query_helpers import careful_query
from backend.utils.query_helpers import dump_results


class OrganizedResource(Resource):

    def get(self):
        result = _query_all()
        all_classes = set(o['product_class'] for o in result)

        grouped = []
        for class_name in all_classes:
            filtered = [o for o in result if o['product_class'] == class_name]
            if len(filtered) > 0:
                total_score = sum([_calc_sth(o) for o in filtered])
                avg_score = total_score / len(filtered)
                grouped.append({
                    'product_class': class_name,
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
    items = Product.query.all()
    return ProductSchema(many=True).dump(items)

def _calc_sth(item):
    weight = item.get('weight_kg')
    volume = item.get('total_volume_m3')
    price = item.get('price')
    if price > 0 and weight and volume:
        return 0.15 * float(weight) + 0.12 * float(volume) / float(price)
    return 10
