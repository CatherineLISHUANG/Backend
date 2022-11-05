from flask_marshmallow import Marshmallow

ma = Marshmallow()


class CitySchema(ma.Schema):
    id = ma.Str()
    name = ma.Str()
