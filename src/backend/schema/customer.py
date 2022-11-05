from flask_marshmallow import Marshmallow

ma = Marshmallow()


class CustomerSchema(ma.Schema):
    id = ma.Str()
    name = ma.Str()
    email_address = ma.Str()
