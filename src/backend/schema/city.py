from flask_marshmallow import Marshmallow

ma = Marshmallow()


class CitySchema(ma.Schema):
    id = ma.Str()
    name = ma.Str()
    post_code = ma.Str()
    latitude = ma.Str()
    longitude = ma.Str()
