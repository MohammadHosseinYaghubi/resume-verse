from django.db import IntegrityError
from django.test import TestCase

from apps.resume.models import (
    Resume,
    SocialLink,
    SocialPlatform,
)


class SocialModelTest(TestCase):

    def setUp(self):

        self.resume = Resume.objects.create(
            full_name="Mohammad",
            slug="mohammad",
        )

    def test_str(self):

        social = SocialLink.objects.create(
            resume=self.resume,
            platform=SocialPlatform.GITHUB,
            url="https://github.com/test",
        )

        self.assertEqual(
            str(social),
            "Mohammad - github",
        )

    def test_default_display_order(self):

        social = SocialLink.objects.create(
            resume=self.resume,
            platform=SocialPlatform.GITHUB,
            url="https://github.com/test",
        )

        self.assertEqual(
            social.display_order,
            0,
        )

    def test_unique_platform_per_resume(self):

        SocialLink.objects.create(
            resume=self.resume,
            platform=SocialPlatform.GITHUB,
            url="https://github.com/test",
        )

        with self.assertRaises(
            IntegrityError,
        ):

            SocialLink.objects.create(
                resume=self.resume,
                platform=SocialPlatform.GITHUB,
                url="https://github.com/test2",
            )