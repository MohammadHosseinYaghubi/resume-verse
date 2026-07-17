from pathlib import Path
from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.resume.models import Resume
from apps.pdf.selectors import (
    pdf_directory,
    resume_pdf_exists,
    resume_pdf_path,
    resume_pdf_url,
)

User = get_user_model()


class PDFSelectorTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            password="12345678",
        )
        
        self.resume = Resume.objects.create(
            user=self.user,
            full_name="Mohsen",
            slug="mohsen",
            title="Backend",
            bio="Bio",
            email="admin@test.com",
            experience="exp",
            education="edu",
        )

    def test_pdf_directory(self):
        self.assertEqual(
            pdf_directory(),
            Path(settings.MEDIA_ROOT) / "pdf" / "resumes",
        )

    def test_resume_pdf_path(self):
        self.assertEqual(
            resume_pdf_path(self.resume),
            Path(settings.MEDIA_ROOT)
            / "pdf"
            / "resumes"
            / "mohsen.pdf",
        )

    def test_resume_pdf_url(self):
        self.assertEqual(
            resume_pdf_url(self.resume),
            f"{settings.MEDIA_URL}pdf/resumes/mohsen.pdf",
        )

    def test_pdf_not_exists(self):
        self.assertFalse(
            resume_pdf_exists(
                self.resume,
            )
        )