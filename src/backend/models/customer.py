import uuid
import sqlalchemy as sa
from .database import db

class Customer(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    first_name = sa.Column(sa.String(150))
    last_name = sa.Column(sa.String(150))
