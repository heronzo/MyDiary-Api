import unittest
import app

class TestApp(unittest.TestCase):
    def test_entries_ndpoint(self):
         res = self.client().get('/bucketlists/')
         self.assertEqual(res.status_code, 200)
        