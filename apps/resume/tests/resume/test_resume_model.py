from django.db import IntegrityError
from django.test import TestCase

from apps.resume.models import Resume


class ResumeModelTest(TestCase):

    def test_create_resume(self):

        resume = Resume.objects.create(
            full_name="Mohammad Hosseini",
            slug="mohammad-hosseini",
        )

        self.assertEqual(
            resume.full_name,
            "Mohammad Hosseini",
        )

    def test_str(self):

        resume = Resume.objects.create(
            full_name="Mohammad Hosseini",
            slug="mohammad-hosseini",
        )

        self.assertEqual(
            str(resume),
            "Mohammad Hosseini",
        )

    def test_unique_slug(self):

        Resume.objects.create(
            full_name="Mohammad",
            slug="mohammad",
        )

        with self.assertRaises(
            IntegrityError,
        ):

            Resume.objects.create(
                full_name="Another",
                slug="mohammad",
            )

    def test_default_public(self):

        resume = Resume.objects.create(
            full_name="Mohammad",
            slug="mohammad",
        )

        self.assertTrue(
            resume.is_public,
        )