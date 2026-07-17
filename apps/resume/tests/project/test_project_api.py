from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

from apps.resume.models import (
    Resume,
    Project,
)

User = get_user_model()


class ProjectAPITestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="admin",
            password="12345678",
        )

        self.resume = Resume.objects.create(
            owner=self.user,
            full_name="Mohsen",
            slug="mohsen",
            title="Backend Developer",
            email="admin@test.com",
        )

        self.project = Project.objects.create(
            resume=self.resume,
            title="Portfolio",
            slug="portfolio",
            description="My Project",
        )

    def test_project_list(self):

        response = self.client.get(
            reverse(
                "project-list",
            )
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_project_detail(self):

        response = self.client.get(
            reverse(
                "project-detail",
                kwargs={
                    "slug": self.project.slug,
                },
            )
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["slug"],
            "portfolio",
        )

    def test_search(self):

        response = self.client.get(
            reverse("project-list"),
            {
                "search": "Portfolio",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_ordering(self):

        response = self.client.get(
            reverse("project-list"),
            {
                "ordering": "title",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_filter_status(self):

        response = self.client.get(
            reverse("project-list"),
            {
                "status": "published",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )