from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

class thingsTests(TestCase):
    def test_home_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_templete(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    # def test_about_page_status_code(self):
    #     url = reverse("snack_detail", args='1')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_about_page_templete(self):
    #     url = reverse('snack_detail', args='1')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'snack_detail.html')
    #     self.assertTemplateUsed(response, 'base.html')
