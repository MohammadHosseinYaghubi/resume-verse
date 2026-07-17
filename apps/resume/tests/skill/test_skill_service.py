from django.test import TestCase

from apps.resume.models import (
    Skill,
    SkillCategory,
)

from apps.resume.services.skill import (
    create_skill,
    update_skill,
    delete_skill,
)


class SkillServiceTest(TestCase):

    def setUp(self):

        self.category = SkillCategory.objects.create(
            name="Backend",
            slug="backend",
        )

    def test_create_skill(self):

        skill = create_skill(
            {
                "name": "Django",
                "category": self.category,
            }
        )

        self.assertEqual(
            skill.slug,
            "django",
        )

    def test_update_skill(self):

        skill = create_skill(
            {
                "name": "Django",
                "category": self.category,
            }
        )

        update_skill(
            skill,
            {
                "name": "FastAPI",
            },
        )

        skill.refresh_from_db()

        self.assertEqual(
            skill.slug,
            "fastapi",
        )

    def test_delete_skill(self):

        skill = create_skill(
            {
                "name": "Django",
                "category": self.category,
            }
        )

        delete_skill(
            skill,
        )

        self.assertEqual(
            Skill.objects.count(),
            0,
        )