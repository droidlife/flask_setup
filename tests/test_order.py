import os
import unittest
from app import create_app
from api.models import db

app = create_app()
flask_app = app.app
client = flask_app.test_client()


class MyTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with flask_app.app_context():
            db.init_app(flask_app)
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        os.remove('/tmp/test.db')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_equal_numbers(self):
        print(client.get('/v1/order', query_string={'customer_email': "a"}))
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
