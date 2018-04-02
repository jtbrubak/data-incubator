import os
import data_incubator
import unittest
import tempfile
from PIL import Image

class TestCase(unittest.TestCase):

    def setUp(self):
        data_incubator.app.config['TESTING'] = True
        self.app = data_incubator.app.test_client()

    def test_image_post(self):

        rv = self.app.get('/')
        assert b'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()
