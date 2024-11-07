import unittest
from ..src.utils import *


class TestPostgreSQL(unittest.TestCase):

    def test_can_connect(self):
        connect()
        result = exec_get_one('SELECT VERSION()')
        self.assertTrue(result[0].startswith('PostgreSQL'))


if __name__ == '__main__':
    unittest.main()
