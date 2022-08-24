from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack

# Create your tests here.
class SnackTests(TestCase):
    def setUp(self):
        purchaser = get_user_model().objects.create(username="yuwei_1st", password="abc123abc123")
        Snack.objects.create(name="Doritos", purchaser=purchaser, description="Doritos is good.")

    def test_list_page_status_code(self):
        url = reverse('showList')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('showList')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('showList')
        response = self.client.get(url)
        things = response.context['object_list']
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0].name, "Doritos")
        self.assertEqual(things[0].description, "Doritos is good.")
        self.assertEqual(things[0].purchaser.username, "yuwei_1st")

    def test_detail_page_status_code(self):
        url = reverse('showDetailList', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('showDetailList', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('showDetailList', args=(1,))
        response = self.client.get(url)
        thing = response.context['snack']
        self.assertEqual(thing.name, "Doritos")
        self.assertEqual(thing.description, "Doritos is good.")
        self.assertEqual(thing.purchaser.username, "yuwei_1st")
