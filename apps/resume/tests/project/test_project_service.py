from django.test import TestCase

from apps.resume.models import (
    Resume,
)

from apps.resume.services.project import (
    create_project,
    update_project,
)


class ProjectServiceTest(TestCase):

    def setUp(self):

        self.resume = Resume.objects.create(
            full_name="Mohsen",
            slug="mohsen",
        )

    def test_create_project(self):

        project = create_project(
            {
                "resume": self.resume,
                "title": "Portfolio",
                "slug": "portfolio",
                "description": "Description",
            }
        )

        self.assertEqual(
            project.slug,
            "portfolio",
        )

    def test_update_project(self):

        project = create_project(
            {
                "resume": self.resume,
                "title": "Portfolio",
                "slug": "portfolio",
                "description": "Description",
            }
        )

        update_project(
            project,
            {
                "title": "New Project",
            },
        )

        project.refresh_from_db()

        self.assertEqual(
            project.title,
            "New Project",
        )