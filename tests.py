from django.contrib.auth import get_user_model
from django.test import TestCase


class PalletsAdminSiteTests(TestCase):
    def test_staff_user_can_access_dashboard(self):
        user = get_user_model().objects.create_user(
            username='staffuser',
            password='testpass123',
            is_staff=True,
            is_superuser=False,
        )

        self.client.force_login(user)
        response = self.client.get('/pallets/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pallets')
