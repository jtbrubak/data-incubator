import data_incubator
import unittest
from io import StringIO

class TestCase(unittest.TestCase):

    def setUp(self):
        data_incubator.app.config['TESTING'] = True
        self.app = data_incubator.app.test_client()

    def test_image_post(self):
        with open('test_image.png') as f:
            raw_img = f.read()
        rv = self.app.post('/image', content_type='multipart/form-data', data={'image': (StringIO(raw_img), 'test_image.png')})
        assert rv.data == raw_img

if __name__ == '__main__':
    unittest.main()
