import unittest
import psycopg2
from dao import Connection 

class TestConnection(unittest.TestCase):
    """PostgreSQL for Python Connector tests."""

    connection = None

    def setUp(self):
        config = {
            user = 'user',
            password = 'password',
            host = 'localhost',
            database = 'test',
            auth_plugin = 'mysql_native_password'
        }
        self.connection = mysql.connector.connect(**config)

    def tearDown(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def test_connection(self):
        self.assertTrue(self.connection.is_connected())

if __name__ == '__main__':
    unittest.main()