from django.test import SimpleTestCase

from rest_framework.exceptions import ValidationError

from apps.resume.api.validators.common import (
    validate_name,
    validate_slug,
)

from apps.resume.api.validators.project import (
    validate_image,
)


class ResumeValidatorTest(SimpleTestCase):

    def test_validate_name(self):

        self.assertEqual(
            validate_name(
                " Mohammad "
            ),
            "Mohammad",
        )

    def test_validate_slug(self):

        self.assertEqual(
            validate_slug(
                " My-Slug "
            ),
            "my-slug",
        )

    def test_empty_name(self):

        with self.assertRaises(
            ValidationError,
        ):

            validate_name("   ")

    def test_invalid_image(self):

        with self.assertRaises(
            ValidationError,
        ):

            validate_image(None)