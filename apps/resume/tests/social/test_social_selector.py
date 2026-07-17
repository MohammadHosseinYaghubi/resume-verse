from django.test import TestCase

from apps.resume.models import (
    Resume,
    SocialLink,
    SocialPlatform,
)

from apps.resume.selectors.social import (
    social_queryset,
    get_social,
)


class SocialSelectorTest(TestCase):

    def setUp(self):

        self.resume = Resume.objects.create(
            full_name="Mohammad",
            slug="mohammad",
        )

        self.social = SocialLink.objects.create(
            resume=self.resume,
            platform=SocialPlatform.GITHUB,
            url="https://github.com/test",
        )

    def test_social_queryset(self):

        queryset = social_queryset()

        self.assertEqual(
            queryset.count(),
            1,
        )

    def test_get_social(self):

        social = get_social(
            self.social.id,
        )

        self.assertEqual(
            social.id,
            self.social.id,
        )