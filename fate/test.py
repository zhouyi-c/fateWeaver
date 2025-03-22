# fate/tests.py
from django.test import TestCase
from django.urls import reverse

class FateAccessTest(TestCase):
    def test_anonymous_access(self):
        response = self.client.get(reverse('fate_index'))
        self.assertRedirects(response, '/users/login/?next=/fate/')