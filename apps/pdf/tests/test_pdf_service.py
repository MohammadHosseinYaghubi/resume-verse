from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.resume.models import Resume
from apps.pdf.services import (
    generate_resume_pdf,
    delete_resume_pdf,
    regenerate_resume_pdf,
    pdf_status,
)

User = get_user_model()


class PDFServiceTestCase(TestCase):

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

    @patch("apps.pdf.services.generator.generate")
    def test_generate_resume_pdf(
        self,
        mock_generate,
    ):

        generate_resume_pdf(
            resume=self.resume,
        )

        mock_generate.assert_called_once()

    @patch("apps.pdf.services.delete_file")
    def test_delete_resume_pdf(
        self,
        mock_delete,
    ):

        delete_resume_pdf(
            resume=self.resume,
        )

        mock_delete.assert_called_once()

    @patch("apps.pdf.services.generate_resume_pdf")
    @patch("apps.pdf.services.delete_resume_pdf")
    def test_regenerate_resume_pdf(
        self,
        mock_delete,
        mock_generate,
    ):

        regenerate_resume_pdf(
            resume=self.resume,
        )

        mock_delete.assert_called_once()

        mock_generate.assert_called_once()

    @patch("apps.pdf.services.resume_pdf_exists")
    def test_pdf_status_ready(
        self,
        mock_exists,
    ):

        mock_exists.return_value = True

        result = pdf_status(
            resume=self.resume,
        )

        self.assertEqual(
            result["status"],
            "ready",
        )

        self.assertIn(
            "download_url",
            result,
        )

    @patch("apps.pdf.services.resume_pdf_exists")
    def test_pdf_status_processing(
        self,
        mock_exists,
    ):

        mock_exists.return_value = False

        result = pdf_status(
            resume=self.resume,
        )

        self.assertEqual(
            result["status"],
            "processing",
        )