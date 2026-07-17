from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

from apps.resume.models import (
    Skill,
    SkillCategory,
)

User = get_user_model()


class SkillAPITestCase(APITestCase):

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

        self.skill = Skill.objects.create(
            name="Django",
            slug="django",
            category=self.category,
        )

    def test_skill_list(self):

        url = reverse("skill-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data),
            1,
        )

    def test_skill_detail(self):

        url = reverse(
            "skill-detail",
            kwargs={
                "id": self.skill.id,
            },
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["name"],
            "Django",
        )

    def test_create_skill_requires_login(self):

        url = reverse("skill-list")

        response = self.client.post(
            url,
            {
                "name": "FastAPI",
                "category": self.category.id,
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_create_skill(self):

        self.client.force_authenticate(
            self.user,
        )

        url = reverse("skill-list")

        response = self.client.post(
            url,
            {
                "name": "FastAPI",
                "category": self.category.id,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            Skill.objects.count(),
            2,
        )

    def test_delete_skill(self):

        self.client.force_authenticate(
            self.user,
        )

        url = reverse(
            "skill-detail",
            kwargs={
                "id": self.skill.id,
            },
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        
    def test_search(self):

        response = self.client.get(
            reverse("skill-list"),
            {
                "search": "Django",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_filter_category(self):

        response = self.client.get(
            reverse("skill-list"),
            {
                "category": self.category.id,
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_ordering(self):

        response = self.client.get(
            reverse("skill-list"),
            {
                "ordering": "name",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )