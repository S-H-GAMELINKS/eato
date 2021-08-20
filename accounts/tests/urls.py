from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import mypage, mypage_edit, mypage_update

class AccountUrlTestCase(TestCase):
    fixtures = ['accounts_url_testdata.json']

    def setUp(self):
        super(AccountUrlTestCase, self).setUp()

    def test_accounts_mypage_url(self):
        url = reverse('accounts:mypage')
        self.assertEqual(resolve(url).func, mypage)

    def test_accounts_mypage_edit_url(self):
        url = reverse('accounts:mypage_edit')
        self.assertEqual(resolve(url).func, mypage_edit)

    def test_accounts_mypage_update_url(self):
        url = reverse('accounts:mypage_update')
        self.assertEqual(resolve(url).func, mypage_update)
