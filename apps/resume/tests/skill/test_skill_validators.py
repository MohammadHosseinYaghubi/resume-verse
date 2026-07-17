from django.test import SimpleTestCase
from rest_framework.exceptions import ValidationError

from apps.resume.api.validators.common import (
    validate_name,
    validate_slug,
)


class SkillValidatorTest(SimpleTestCase):

    def test_validate_name(self):

        value = validate_name(
            " Django "
        )

        self.assertEqual(
            value,
            "Django",
        )

    def test_empty_name(self):

        with self.assertRaises(
            ValidationError,
        ):

            validate_name(
                "   "
            )

    def test_validate_slug(self):

        value = validate_slug(
            " django "
        )

        self.assertEqual(
            value,
            "django",
        )