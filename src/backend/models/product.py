import uuid
import sqlalchemy as sa
from .database import db


class Product(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    code = sa.Column(sa.String(150))

    product_class = sa.Column(sa.String(150))
    name = sa.Column(sa.String(150))
    price = sa.Column(sa.Float)
    sales_unit = sa.Column(sa.String(150))

    weight_kg = sa.Column(sa.Float)
    total_volume_m3 = sa.Column(sa.Float)

    # Relations
    orders_made = db.relationship(
        'Order', backref='product')

    @property
    def full_info(self):
        return f'{self.name} ({self.product_class})'
