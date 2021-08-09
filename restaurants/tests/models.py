from django.test import TestCase
from django.urls import reverse
from restaurants.models import Restaurant

# Create your tests here.
class RestaurantModelTestCase(TestCase):
    fixtures = ['restaurants_model_testdata.json']
    
    def setUp(self):
        super(RestaurantModelTestCase, self).setUp()
        self.restaurant_1 = Restaurant.objects.get(pk=1)
        self.valid_name = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        self.valid_address = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        self.valid_tel_number = 'xxxxxxxxxxxxxxxxxxxx'

    def test_isnot_empty(self):
        restaurants = Restaurant.objects.all()
        self.assertEqual(restaurants.count(), 1)

    def test_fixture(self):
        self.assertEqual(self.restaurant_1.name, 'restaurant')
        self.assertEqual(self.restaurant_1.address, 'restaurant')
        self.assertEqual(self.restaurant_1.tel_number, 'XXX-XXXX-XXXX')

    def test_create_restaurant_only_name(self):
        r = Restaurant(name=self.valid_name)
        r.save()
        save_restaurant = Restaurant.objects.last()
        self.assertEqual(save_restaurant.name, self.valid_name)

    def test_create_restaurant_only_address(self):
        r = Restaurant(address=self.valid_address)
        r.save()
        save_restaurant = Restaurant.objects.last()
        self.assertEqual(save_restaurant.address, self.valid_address)

    def test_create_restaurant_only_tel_number(self):
        r = Restaurant(tel_number=self.valid_tel_number)
        r.save()
        save_restaurant = Restaurant.objects.last()
        self.assertEqual(save_restaurant.tel_number, self.valid_tel_number)

    def test_create_restaurant(self):        
        r = Restaurant(name=self.valid_name, address=self.valid_address, tel_number=self.valid_tel_number)
        r.save()
        restaurants = Restaurant.objects.all()
        save_restaurant = Restaurant.objects.last()
        self.assertEqual(save_restaurant.name, self.valid_name)
        self.assertEqual(save_restaurant.address, self.valid_address)
        self.assertEqual(save_restaurant.tel_number, self.valid_tel_number)
