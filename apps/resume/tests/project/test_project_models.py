from django.test import TestCase

from apps.resume.models import (
    Project,
    ProjectStatus,
    Resume,
)


class ProjectModelTest(TestCase):

    def setUp(self):

        self.resume = Resume.objects.create(
            full_name="Mohsen",
            slug="mohsen",
        )

    def test_create_project(self):

        project = Project.objects.create(
            resume=self.resume,
            title="Portfolio",
            slug="portfolio",
            description="Description",
        )

        self.assertEqual(
            project.title,
            "Portfolio",
        )

    def test_str(self):

        project = Project.objects.create(
            resume=self.resume,
            title="Portfolio",
            slug="portfolio",
            description="Description",
        )

        self.assertEqual(
            str(project),
            "Portfolio",
        )

    def test_default_status(self):

        project = Project.objects.create(
            resume=self.resume,
            title="Portfolio",
            slug="portfolio",
            description="Description",
        )

        self.assertEqual(
            project.status,
            ProjectStatus.PUBLISHED,
        )

    def test_embed_url_property(self):

        project = Project.objects.create(
            resume=self.resume,
            title="Portfolio",
            slug="portfolio",
            description="Description",
        )

        self.assertEqual(
            project.embed_url,
            project.get_embed_url(),
        )