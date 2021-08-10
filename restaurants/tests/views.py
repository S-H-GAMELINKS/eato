from django.test import TestCase
from django.urls import reverse
from restaurants.models import Restaurant

class RestaurantViewTestCase(TestCase):
    fixtures = ['restaurants_view_testdata.json']

    def setUp(self):
        super(RestaurantViewTestCase, self).setUp()
        self.restaurant_1 = Restaurant.objects.get(pk=1)
        self.assert_name = self.restaurant_1.name
        self.assert_address = self.restaurant_1.address
        self.assert_tel_number = self.restaurant_1.tel_number

    def test_restaurants_index_view_response(self):
        url = reverse('restaurants:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.assert_name)
        self.assertContains(response, self.assert_address)
        self.assertNotContains(response, self.assert_tel_number)

    def test_restaurants_detail_view_response(self):
        url = reverse('restaurants:detail', args=(self.restaurant_1.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.assert_name)
        self.assertContains(response, self.assert_address)
        self.assertContains(response, self.assert_tel_number)
