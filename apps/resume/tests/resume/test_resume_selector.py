from django.test import TestCase

from apps.resume.models import Resume

from apps.resume.selectors.resume import (
    get_resume,
    resume_queryset,
)


class ResumeSelectorTest(TestCase):

    def setUp(self):

        self.resume = Resume.objects.create(
            full_name="Mohammad",
            slug="mohammad",
        )

    def test_resume_queryset(self):

        self.assertEqual(
            resume_queryset().count(),
            1,
        )

    def test_get_resume(self):

        resume = get_resume(
            self.resume.slug,
        )

        self.assertEqual(
            resume.slug,
            "mohammad",
        )

    def test_prefetch_skills(self):

        resume = resume_queryset().first()

        self.assertIsNotNone(
            resume.skills,
        )

    def test_prefetch_projects(self):

        resume = resume_queryset().first()

        self.assertIsNotNone(
            resume.projects,
        )

    def test_prefetch_social_links(self):

        resume = resume_queryset().first()

        self.assertIsNotNone(
            resume.social_links,
        )