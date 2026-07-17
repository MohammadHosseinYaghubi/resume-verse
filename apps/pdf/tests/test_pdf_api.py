from unittest.mock import patch

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

from apps.resume.models import Resume

User = get_user_model()


class PDFAPITestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="admin",
            password="12345678",
        )

        self.resume = Resume.objects.create(
            user=self.user,
            full_name="Mohsen",
            slug="mohsen",
            title="Backend Developer",
            bio="Bio",
            email="admin@test.com",
            experience="Experience",
            education="Education",
        )

        self.client.force_authenticate(
            self.user,
        )

    @patch("apps.pdf.api.views.enqueue_resume_pdf")
    def test_generate_pdf(
        self,
        mock_enqueue,
    ):

        url = reverse(
            "pdf-generate",
        )

        response = self.client.post(
            url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        mock_enqueue.assert_called_once()

    @patch("apps.pdf.api.views.pdf_status")
    def test_status(
        self,
        mock_status,
    ):

        mock_status.return_value = {

            "status": "ready",

            "download_url": "/media/pdf/resumes/mohsen.pdf",

        }

        url = reverse(
            "pdf-status",
        )

        response = self.client.get(
            url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["status"],
            "ready",
        )

    @patch("apps.pdf.api.views.open")
    @patch("apps.pdf.api.views.resume_pdf_path")
    def test_download(
        self,
        mock_path,
        mock_open,
    ):

        mock_path.return_value = "/tmp/resume.pdf"

        mock_open.return_value = open(__file__, "rb")

        url = reverse(
            "pdf-download",
        )

        response = self.client.get(
            url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_anonymous_generate(self):

        self.client.logout()

        url = reverse(
            "pdf-generate",
        )

        response = self.client.post(
            url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_anonymous_status(self):

        self.client.logout()

        url = reverse(
            "pdf-status",
        )

        response = self.client.get(
            url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )