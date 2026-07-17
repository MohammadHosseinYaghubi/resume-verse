from django.test import TestCase

from apps.resume.models import (
    Resume,
    SocialPlatform,
)

from apps.resume.services.social import (
    create_social,
    update_social,
)


class SocialServiceTest(TestCase):

    def setUp(self):

        self.resume = Resume.objects.create(
            full_name="Mohammad",
            slug="mohammad",
        )

    def test_create_social(self):

        social = create_social(
            {
                "resume": self.resume,
                "platform": SocialPlatform.GITHUB,
                "url": "https://github.com/test",
            }
        )

        self.assertEqual(
            social.platform,
            SocialPlatform.GITHUB,
        )

    def test_update_social(self):

        social = create_social(
            {
                "resume": self.resume,
                "platform": SocialPlatform.GITHUB,
                "url": "https://github.com/test",
            }
        )

        update_social(
            social,
            {
                "url": "https://github.com/new",
            },
        )

        social.refresh_from_db()

        self.assertEqual(
            social.url,
            "https://github.com/new",
        )