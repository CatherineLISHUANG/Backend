import uuid
import sqlalchemy as sa
from .database import db


class Freight(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    code = sa.Column(sa.String(150))

    # Foreign keys
    departure_city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    arrival_city_id = db.Column(db.Integer, db.ForeignKey('city.id'))

    departure_city = db.relationship("City", foreign_keys=[departure_city_id])
    arrival_city = db.relationship("City", foreign_keys=[arrival_city_id])

    # Below can be calculated
    pre_calc_distance = sa.Column(sa.Float)
    pre_calc_weight = sa.Column(sa.Float)
    pre_calc_volume = sa.Column(sa.Float)
    pre_calc_price = sa.Column(sa.Float)

    date = sa.Column(sa.Date)
