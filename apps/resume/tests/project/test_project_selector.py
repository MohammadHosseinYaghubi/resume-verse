from django.test import TestCase

from apps.resume.models import (
    Resume,
    Project,
)

from apps.resume.selectors.project import (
    get_project,
    project_queryset,
    published_projects,
)


class ProjectSelectorTest(TestCase):

    def setUp(self):

        self.resume = Resume.objects.create(
            full_name="Mohsen",
            slug="mohsen",
        )

        self.project = Project.objects.create(
            resume=self.resume,
            title="Portfolio",
            slug="portfolio",
            description="Description",
        )

    def test_project_queryset(self):

        self.assertEqual(
            project_queryset().count(),
            1,
        )

    def test_published_projects(self):

        self.assertEqual(
            published_projects().count(),
            1,
        )

    def test_get_project(self):

        project = get_project(
            self.project.slug,
        )

        self.assertEqual(
            project.slug,
            "portfolio",
        )