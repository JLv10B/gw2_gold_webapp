from django.core.management import call_command
from django.test import TestCase, Client, override_settings
from unid_processing import views
from django.urls import reverse
from django.test.utils import setup_test_environment


class DataDumpViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_data_dump_view(self):
        # Call the view using the client
        response = self.client.get(reverse('data_dump'))

        # Check the content type
        self.assertEqual(response.get('Content-Type'), 'text/plain')

        # Check the content disposition
        self.assertEqual(response.get('Content-Disposition'), 'attachment; filename="test.txt"')

        # Check the content of the response (assuming lines are not modified)
        expected_content = b"This is line 1\nThis is line 2\nthis is line 3\n"
        self.assertEqual(response.content, expected_content)