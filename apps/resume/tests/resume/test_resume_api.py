from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.resume.models import Resume


class ResumeAPITest(APITestCase):

    def setUp(self):

        self.resume = Resume.objects.create(
            full_name="Mohammad",
            slug="mohammad",
        )

    def test_list(self):

        response = self.client.get(
            reverse(
                "resume-list",
            )
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_detail(self):

        response = self.client.get(
            reverse(
                "resume-detail",
                kwargs={
                    "slug": self.resume.slug,
                },
            )
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_search(self):

        response = self.client.get(
            reverse("resume-list"),
            {
                "search": "Mohammad",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_ordering(self):

        response = self.client.get(
            reverse("resume-list"),
            {
                "ordering": "-created_at",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_filter_public(self):

        response = self.client.get(
            reverse("resume-list"),
            {
                "is_public": True,
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )