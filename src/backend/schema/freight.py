from flask_marshmallow import Marshmallow
from .city import CitySchema

ma = Marshmallow()


class FreightSchema(ma.Schema):
    id = ma.Str()
    departure_city = ma.Nested(CitySchema)
    arrival_city = ma.Nested(CitySchema)
