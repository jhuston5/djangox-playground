from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from drills.models import Drill

# Create your tests here.
'''
drill_date = models.DateTimeField(blank=True, null=True)
  soldier = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  location = models.CharField(max_length=64)
  description = models.TextField(default='')'''
class DrillsTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.drill = Drill.objects.create(
            drill_date = '03-03-2022', soldier=self.user, location = 'MURC', description = "MAR IDT")

    def test_string_representation(self):
        self.assertEqual(str(self.drill), 'tester')

    def test_drill_name(self):
        self.assertEqual(f'{self.drill.username}', 'tester')

    def test_drill_description(self):
        self.assertEqual(f'{self.drill.description}', 'MAR IDT')
    
    def test_username(self):
        self.assertEqual(f'{self.user.username}', 'tester')

    def test_user_email(self):
        self.assertEqual(f'{self.user.email}', 'tester@email.com')

    def test_list_page_status_code(self):
        url = reverse("drill_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("drill_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "drill_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_detail_page_status_code(self):
        url = reverse('drill_detail', args="1")
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_update_page_status_code(self):
        url = reverse('drill_update', args="1")
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)
      
    def test_delete_page_status_code(self):
      url = reverse('drill_delete', args="1")
      response = self.client.get(url)
      print(response)
      self.assertEqual(response.status_code, 200)

    # def test_drill_create_view(self):
    #     response = self.client.post(
    #         reverse("drill_create"),
    #         {
    #             "name": "Licorice",
    #             "description": "test",
    #             "purchaser": self.user.id,
    #         }, follow=True
    #     )

    #     self.assertRedirects(response, reverse("drill_detail", args="2"))
    #     self.assertContains(response, "Details about Licorice")