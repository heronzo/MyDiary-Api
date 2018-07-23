import unittest
import app

class TestApp(unittest.TestCase):
    with app.test_entries_endpoint() as e:
        response = e.get('/some/path/that/exists')
        self.assertEquals(response.status_code, 200)
       

