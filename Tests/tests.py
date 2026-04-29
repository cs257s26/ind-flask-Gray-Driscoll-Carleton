import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    #Copied from the flask lab
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_avg_schooling_valid_country(self):
        response = self.app.get('/avgSchooling/Canada')
        self.assertEqual(response.status_code, 200)
        self.assertIn('avg_schooling', response.data.decode())

    def test_avg_schooling_invalid_country(self):
        response = self.app.get('/avgSchooling/Dorne')
        self.assertEqual(response.status_code, 200)
        self.assertIn('[]', response.data.decode())  #Returns nothing because the list is empty (DNI)

    def test_avg_schooling_no_country(self):
        response = self.app.get('/avgSchooling/')
        self.assertEqual(response.status_code, 404)
        self.assertIn('', response.data.decode())   #We should get an error and have nothing returned but an error message

    def test_lit_growth_valid_country(self):
        response = self.app.get('/litGrowth/Canada')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Canada', response.data.decode())

    def test_lit_growth_invalid_country(self):
        response = self.app.get('/litGrowth/HighGarden')
        self.assertEqual(response.status_code, 200)
        self.assertIn('No literacy data for this country', response.data.decode()) #Lola wrote a special response statement so we do not simply check for brackets
        
    def test_lit_growth_no_country(self):
        response = self.app.get('/litGrowth/')
        self.assertEqual(response.status_code, 404)
        self.assertIn('', response.data.decode())

if __name__ == '__main__':
    unittest.main()