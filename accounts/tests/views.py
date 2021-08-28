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
        self.assertContains(response, 'プロフィール')
        self.assertContains(response, 'お気に入り')
        self.assertContains(response, 'クチコミレビュー')
        self.assertContains(response, self.restaurant.name)
        self.assertContains(response, self.restaurant.address)

    def test_accounts_mypage_edit_view_response_with_anonymous_user(self):
        url = reverse('accounts:mypage_edit')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_accounts_mypage_edit_view_response_with_login_user(self):
        client = Client()
        client.force_login(self.user)
        url = reverse('accounts:mypage_edit')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Email')
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.email)

    def test_accounts_mypage_update_view_response_with_anonymous_user(self):
        url = reverse('accounts:mypage_update')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

    def test_accounts_mypage_update_view_response_with_login_user(self):
        client = Client()
        client.force_login(self.user)
        url = reverse('accounts:mypage_update')

        response = client.post(url, data={'name': 'user2', 'email': 'user2@example.com', 'bio': 'HALO2'})
        user = User.objects.get(pk=1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.username, 'user2')
        self.assertEqual(user.email, 'user2@example.com')
        self.assertEqual(user.profile.bio, 'HALO2')

    def test_accounts_mypage_detail(self):
        url = reverse('accounts:detail', kwargs={'user_id': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.email)
