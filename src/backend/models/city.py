import uuid
import sqlalchemy as sa
from .database import db


class City(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    post_code = sa.Column(sa.String(150))
    name = sa.Column(sa.String(150))

    # Add later
    latitude = sa.Column(sa.String(150))
    longitude = sa.Column(sa.String(150))

    # Relations
    orders_made = db.relationship(
        'Order', backref='city')

    # freights_as_departure = db.relationship(
    #     'Freight', backref='departure_city_id')
    # freights_as_arrival = db.relationship(
    #     'Freight', backref='arrival_city')
