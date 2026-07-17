from django.test import TestCase

from apps.resume.models import (
    Skill,
    SkillCategory,
)

from apps.resume.selectors.skill import (
    category_skills,
    get_skill,
    search_skills,
    skill_queryset,
)


class SkillSelectorTest(TestCase):

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

    def test_skill_queryset(self):

        self.assertEqual(
            skill_queryset().count(),
            1,
        )

    def test_get_skill(self):

        obj = get_skill(
            self.skill.id,
        )

        self.assertEqual(
            obj.id,
            self.skill.id,
        )

    def test_category_skills(self):

        queryset = category_skills(
            self.category.id,
        )

        self.assertEqual(
            queryset.count(),
            1,
        )

    def test_search_skills(self):

        queryset = search_skills(
            "Djan",
        )

        self.assertEqual(
            queryset.count(),
            1,
        )