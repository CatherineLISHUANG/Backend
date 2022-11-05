import os
import unittest

from backend.server import create_app
from sample_data import get_sample_data


class EndpointTestBaseClass(unittest.TestCase):

    file_path = '/tmp/tmp_test.db'

    def setUp(self):
        from backend.models.database import db
        self.db = db
        self._create_flask_app()
        self._create_database()
        self.endpoint_client = self.flask_app.test_client()

    def tearDown(self):
        os.unlink(self.file_path)

    def _create_flask_app(self):
        self.flask_app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{self.file_path}"})

    def _create_database(self):
        with self.flask_app.app_context():
            sample_data = get_sample_data()
            self.db.session.add_all(sample_data)
            self.db.session.commit()
