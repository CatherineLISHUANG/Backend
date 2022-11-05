from flask_marshmallow import Marshmallow
from .city import CitySchema
from .customer import CustomerSchema
from .product import ProductSchema

ma = Marshmallow()


class OrderSchema(ma.Schema):
    id = ma.Str()

    code = ma.Str()
    date = ma.Date()
    product_quantity = ma.Int()

    # Nested
    city = ma.Nested(CitySchema)
    customer = ma.Nested(CustomerSchema)
    product = ma.Nested(ProductSchema)

    # Special
    status = ma.Str()
