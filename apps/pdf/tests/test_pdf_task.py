from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.resume.models import Resume

from apps.pdf.tasks import (
    generate_resume_pdf_task,
)

User = get_user_model()


class PDFTaskTestCase(TestCase):

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

    @patch("apps.pdf.tasks.generate_resume_pdf")
    def test_generate_resume_pdf_task(
        self,
        mock_generate,
    ):

        generate_resume_pdf_task(
            str(self.resume.id),
        )

        mock_generate.assert_called_once()

    @patch("apps.pdf.tasks.generate_resume_pdf")
    def test_generate_resume_pdf_task_called_with_resume(
        self,
        mock_generate,
    ):

        generate_resume_pdf_task(
            str(self.resume.id),
        )

        args = mock_generate.call_args.kwargs

        self.assertEqual(
            args["resume"].id,
            self.resume.id,
        )