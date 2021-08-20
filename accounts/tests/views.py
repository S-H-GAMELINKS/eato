from django.test import TestCase, Client
from django.urls import reverse
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import User, AnonymousUser
from restaurants.models import Restaurant, Favorite

class AccountViewTestCase(TestCase):
    fixtures = ['accounts_view_testdata.json']

    def setUp(self):
        super(AccountViewTestCase, self).setUp()
        self.user = User.objects.get(pk=1)
        self.restaurant = Restaurant.objects.get(pk=1)
        self.favorite = Favorite.objects.get(pk=1)

    def test_accounts_mypage_view_response_with_anonymous_user(self):
        url = reverse('accounts:mypage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_accounts_mypage_view_response_with_login_user(self):
        client = Client()
        client.force_login(self.user)
        url = reverse('accounts:mypage')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile')
        self.assertContains(response, 'Favorite')
        self.assertContains(response, 'Review')
        self.assertContains(response, self.restaurant.name)
        self.assertContains(response, self.restaurant.address)

        