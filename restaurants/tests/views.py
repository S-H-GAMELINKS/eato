from django.test import TestCase
from django.urls import reverse

class RestaurantView(TestCase):
    def test_restaurants_index_view_response(self):
        url = reverse('restaurants:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
