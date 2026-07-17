from django.db import IntegrityError
from django.test import TestCase

from apps.resume.models import (
    Skill,
    SkillCategory,
)


class SkillModelTest(TestCase):

    def setUp(self):

        self.category = SkillCategory.objects.create(
            name="Backend",
            slug="backend",
        )

    def test_str(self):

        skill = Skill.objects.create(
            name="Django",
            slug="django",
            category=self.category,
        )

        self.assertEqual(
            str(skill),
            "Django",
        )

    def test_ordering(self):

        Skill.objects.create(
            name="Python",
            slug="python",
            category=self.category,
        )

        Skill.objects.create(
            name="Django",
            slug="django",
            category=self.category,
        )

        skills = list(
            Skill.objects.all()
        )

        self.assertEqual(
            skills[0].name,
            "Django",
        )

    def test_unique_skill_per_category(self):

        Skill.objects.create(
            name="Django",
            slug="django",
            category=self.category,
        )

        with self.assertRaises(
            IntegrityError,
        ):

            Skill.objects.create(
                name="Django",
                slug="django-2",
                category=self.category,
            )