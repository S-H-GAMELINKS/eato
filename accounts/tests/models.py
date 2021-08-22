from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AccountModelTestCase(TestCase):
    fixtures = ['accounts_model_testdata.json']

    def setUp(self):
        super(AccountModelTestCase, self).setUp()
        self.user = User.objects.get(pk=1)
        self.username = 'user1'
        self.email = 'user1@example.com'
        self.bio = 'user1bio'

    def test_isnot_empty(self):
        users = User.objects.all()
        self.assertEqual(users.count(), 1)

    def test_fixture(self):
        self.assertEqual(self.user.username, self.username)
        self.assertEqual(self.user.email, self.email)
        self.assertEqual(self.user.profile.bio, self.bio)

    def test_update_accounts(self):
        user = self.user
        user.username = 'user2'
        user.email = 'user2@example.com'
        user.profile.bio = 'user2bio'
        user.save()
        self.assertNotEqual(user.username, self.username)
        self.assertNotEqual(user.email, self.email)
        self.assertNotEqual(user.profile.bio, self.bio)
