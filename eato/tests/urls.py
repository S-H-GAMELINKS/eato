from django.test import TestCase
from django.urls import reverse, resolve
from eato.views import lp

class EatoUrlTestCase(TestCase):
    # fixtures = ['eato_url_testdata.json']

    def setUp(self):
        super(EatoUrlTestCase, self).setUp()

    def test_eato_lp_url(self):
        url = reverse('lp')
        self.assertEqual(resolve(url).func, lp)
