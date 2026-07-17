from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

from apps.resume.models import SkillCategory

User = get_user_model()


class SkillCategoryAPITestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_superuser(
            username="admin",
            email="admin@test.com",
            password="12345678",
        )

        self.category = SkillCategory.objects.create(
            name="Backend",
            slug="backend",
        )

    def test_category_list(self):

        url = reverse("skill-category-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_category_detail(self):

        url = reverse(
            "skill-category-detail",
            kwargs={
                "id": self.category.id,
            },
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_create_category(self):

        self.client.force_authenticate(
            self.user,
        )

        url = reverse("skill-category-list")

        response = self.client.post(
            url,
            {
                "name": "Frontend",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

    def test_delete_category(self):

        self.client.force_authenticate(
            self.user,
        )

        url = reverse(
            "skill-category-detail",
            kwargs={
                "id": self.category.id,
            },
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )