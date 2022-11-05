from flask_marshmallow import Marshmallow

ma = Marshmallow()


class CustomerSchema(ma.Schema):
    id = ma.Str()
    first_name = ma.Str()
    last_name = ma.Str()
