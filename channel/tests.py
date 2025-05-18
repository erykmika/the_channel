from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class DashboardViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        user.set_password("12345")
        user.save()
        self.client.login(username="testuser", password="12345")
        self.url = reverse("dashboard")

    def test_dashboard_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "dashboard.html")


class RoomViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.user.set_password("12345")
        self.user.save()
        self.client.login(username="testuser", password="12345")
        self.url = reverse("room", kwargs={"first": "testuser", "second": "otheruser"})

    def test_room_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_room_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "room.html")

    def test_room_view_context_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context["first_user"], "testuser")
        self.assertEqual(response.context["second_user"], "otheruser")
