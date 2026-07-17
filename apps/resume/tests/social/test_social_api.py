from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from apps.resume.models import (
    Resume,
    SocialLink,
    SocialPlatform,
)


class SocialAPITest(APITestCase):

    def setUp(self):

        self.resume = Resume.objects.create(
            full_name="Mohammad",
            slug="mohammad",
        )

        self.social = SocialLink.objects.create(
            resume=self.resume,
            platform=SocialPlatform.GITHUB,
            url="https://github.com/test",
        )

    def test_list_socials(self):

        url = reverse(
            "social-list",
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_detail_social(self):

        url = reverse(
            "social-detail",
            kwargs={
                "id": self.social.id,
            },
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_invalid_social_url(self):

        url = reverse(
            "social-list",
        )

        response = self.client.post(
            url,
            {
                "resume": self.resume.id,
                "platform": SocialPlatform.GITHUB,
                "url": "https://linkedin.com/user",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )