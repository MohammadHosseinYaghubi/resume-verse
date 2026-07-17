from django.test import SimpleTestCase
from rest_framework.exceptions import ValidationError

from apps.resume.api.validators.social import (
    validate_social_url,
)

from apps.resume.models import SocialPlatform


class SocialValidatorTest(SimpleTestCase):

    def test_valid_url(self):

        validate_social_url(
            SocialPlatform.GITHUB,
            "https://github.com/user",
        )

    def test_invalid_url(self):

        with self.assertRaises(
            ValidationError,
        ):

            validate_social_url(
                SocialPlatform.GITHUB,
                "https://linkedin.com/user",
            )