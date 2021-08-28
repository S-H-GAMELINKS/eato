from django.test import TestCase, Client
from django.urls import reverse
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import User, AnonymousUser
from restaurants.models import Restaurant, Favorite, Review
from restaurants.views import favorites

class RestaurantViewTestCase(TestCase):
    fixtures = ['restaurants_view_testdata.json']

    def setUp(self):
        super(RestaurantViewTestCase, self).setUp()
        self.user = User.objects.get(pk=1)
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

    def test_restaurants_favorites_view_url_with_anonymous_user(self):
        url = reverse('restaurants:favorites', kwargs={'restaurant_id': self.restaurant_1.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        count = Favorite.objects.all().count()
        self.assertEqual(count, 1)

    def test_restaurants_favorites_view_url_with_login_user(self):
        client = Client()
        client.force_login(self.user)
        url = reverse('restaurants:favorites', kwargs={'restaurant_id': self.restaurant_1.id})
        response = client.post(url)
        self.assertEqual(response.status_code, 302)
        count = Favorite.objects.all().count()
        last = Favorite.objects.last()
        self.assertEqual(count, 1)
        self.assertEqual(last.restaurant.id, self.restaurant_1.id)
        self.assertEqual(last.user.id, self.user.id)

    def test_restaurants_reviews_view_url_with_anonymous_user(self):
        url = reverse('restaurants:reviews', kwargs={'restaurant_id': self.restaurant_1.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        count = Review.objects.all().count()
        self.assertEqual(count, 1)

    def test_restaurants_reviews_view_url_with_login_user(self):
        client = Client()
        client.force_login(self.user)
        url = reverse('restaurants:reviews', kwargs={'restaurant_id': self.restaurant_1.id})
        response = client.post(url, data={'content': 'HALO2'})
        self.assertEqual(response.status_code, 302)
        count = Review.objects.all().count()
        last = Review.objects.last()
        self.assertEqual(count, 2)
        self.assertEqual(last.restaurant.id, self.restaurant_1.id)
        self.assertEqual(last.user.id, self.user.id)
        self.assertEqual(last.content, "HALO2")
