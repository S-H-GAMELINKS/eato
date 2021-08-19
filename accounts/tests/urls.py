from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import mypage

class AccountUrlTestCase(TestCase):
    fixtures = ['accounts_url_testdata.json']

    def setUp(self):
        super(AccountUrlTestCase, self).setUp()

    def test_accounts_mypage_url(self):
        url = reverse('accounts:mypage')
        self.assertEqual(resolve(url).func, mypage)
