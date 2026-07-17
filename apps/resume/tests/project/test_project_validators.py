from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase

from rest_framework.exceptions import ValidationError

from apps.resume.api.validators.project import (
    validate_project_url,
)


class ProjectValidatorTest(SimpleTestCase):

    def test_valid_project_url(self):

        value = validate_project_url(
            "https://github.com/test/project",
        )

        self.assertEqual(
            value,
            "https://github.com/test/project",
        )

    def test_invalid_project_url(self):

        with self.assertRaises(
            ValidationError,
        ):

            validate_project_url(
                "http://github.com/test/project",
            )