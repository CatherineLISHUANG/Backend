import uuid
import sqlalchemy as sa
from .database import db


class Customer(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    code = sa.Column(sa.String(150))
    # Can be a company
    name = sa.Column(sa.String(150))
    email_address = sa.Column(sa.String(150))

    # Relations
    orders_made = db.relationship(
        'Order', backref='customer')
