from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from accounts.views import mypage, mypage_edit, mypage_update, detail

class AccountUrlTestCase(TestCase):
    fixtures = ['accounts_url_testdata.json']

    def setUp(self):
        super(AccountUrlTestCase, self).setUp()
        self.user = User.objects.get(pk=1)

    def test_accounts_mypage_url(self):
        url = reverse('accounts:mypage')
        self.assertEqual(resolve(url).func, mypage)

    def test_accounts_mypage_edit_url(self):
        url = reverse('accounts:mypage_edit')
        self.assertEqual(resolve(url).func, mypage_edit)

    def test_accounts_mypage_update_url(self):
        url = reverse('accounts:mypage_update')
        self.assertEqual(resolve(url).func, mypage_update)

    def test_accounts_mypage_detail_url(self):
        url = reverse('accounts:detail', kwargs={'user_id': self.user.id})
        self.assertEqual(resolve(url).func, detail)
