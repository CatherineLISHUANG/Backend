from flask_marshmallow import Marshmallow
from .city import CitySchema

ma = Marshmallow()


class FreightSchema(ma.Schema):
    id = ma.Str()
    code = ma.Str()
    departure_city = ma.Nested(CitySchema)
    arrival_city = ma.Nested(CitySchema)

    pre_calc_distance = ma.Float()
    pre_calc_weight = ma.Float()
    pre_calc_volume = ma.Float()
    pre_calc_price = ma.Float()

    date = ma.Date()
