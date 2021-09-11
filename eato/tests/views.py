from django.test import TestCase, Client
from django.urls import reverse

class EatoViewTestCase(TestCase):

    def setUp(self):
        super(EatoViewTestCase, self).setUp()

    def test_lp_hotpper_licesen(self):
        url = reverse('lp')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ホットペッパー Webサービス')
