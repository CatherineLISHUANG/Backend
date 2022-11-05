import uuid
import sqlalchemy as sa
from .database import db


class Order(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    date = sa.Column(sa.Date)
    product_quantity = sa.Column(sa.Integer)

    # Foreign keys
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
