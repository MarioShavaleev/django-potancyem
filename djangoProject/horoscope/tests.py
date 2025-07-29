from django.test import TestCase

# Create your tests here.
class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_leo(self):
        response = self.client.get('/horoscope/leo')
        self.assertEqual(response.status_code, 301)