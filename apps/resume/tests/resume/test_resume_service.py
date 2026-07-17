from django.test import TestCase

from apps.resume.models import (
    Resume,
    Skill,
    SkillCategory,
)

from apps.resume.services.resume import (
    create_resume,
    update_resume,
)


class ResumeServiceTest(TestCase):

    def setUp(self):

        self.category = SkillCategory.objects.create(
            name="Backend",
            slug="backend",
        )

        self.skill = Skill.objects.create(
            name="Django",
            slug="django",
            category=self.category,
        )

    def test_create_resume(self):

        resume = create_resume(
            {
                "full_name": "Mohammad",
                "slug": "mohammad",
                "skills": [
                    self.skill,
                ],
            }
        )

        self.assertEqual(
            resume.skills.count(),
            1,
        )

    def test_update_resume(self):

        resume = create_resume(
            {
                "full_name": "Mohammad",
                "slug": "mohammad",
            }
        )

        update_resume(
            resume,
            {
                "full_name": "Ali",
            },
        )

        resume.refresh_from_db()

        self.assertEqual(
            resume.full_name,
            "Ali",
        )