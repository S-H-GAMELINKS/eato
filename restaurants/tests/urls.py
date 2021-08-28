from django.test import TestCase
from django.urls import reverse, resolve
from restaurants.models import Restaurant, Review
from restaurants.views import index, detail, favorites, likes

class RestaurantUrlTestCase(TestCase):
    fixtures = ['restaurants_url_testdata.json']

    def setUp(self):
        super(RestaurantUrlTestCase, self).setUp()
        self.restaurant_1 = Restaurant.objects.get(pk=1)
        self.review_1 = Review.objects.get(pk=1)

    def test_restaurants_index_url(self):
        url = reverse('restaurants:index')
        self.assertEqual(resolve(url).func, index)

    def test_restaurants_detail_url(self):
        url = reverse('restaurants:detail', args=(self.restaurant_1.id,))
        self.assertEqual(resolve(url).func, detail)

    def test_restaurants_favorites_url(self):
        url = reverse('restaurants:favorites', kwargs={'restaurant_id': self.restaurant_1.id})
        self.assertEqual(resolve(url).func, favorites)

    def test_restaurants_likes_url(self):
        url = reverse('restaurants:likes', kwargs={'restaurant_id': self.restaurant_1.id, 'review_id': self.review_1.id})
