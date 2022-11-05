from flask_marshmallow import Marshmallow

ma = Marshmallow()


class ProductSchema(ma.Schema):
    id = ma.Str()
    code = ma.Str()

    product_class = ma.Str()
    name = ma.Str()
    price = ma.Float()
    sales_unit = ma.String()
    # ...etc...
