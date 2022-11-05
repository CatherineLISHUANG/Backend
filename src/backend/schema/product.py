from flask_marshmallow import Marshmallow

ma = Marshmallow()


class ProductSchema(ma.Schema):
    id = ma.Str()
    code = ma.Str()

    product_class = ma.Str()
    name = ma.Str()
    price = ma.Float()
    sales_unit = ma.String()
    full_info = ma.String()
    weight_kg = ma.Float()
    total_volume_m3 = ma.Float()
    # ...etc...
