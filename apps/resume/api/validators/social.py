from urllib.parse import urlparse

from rest_framework import serializers

from apps.resume.constants import SOCIAL_DOMAINS


def validate_social_url(
    platform,
    url,
):

    domain = urlparse(url).netloc.lower()

    expected = SOCIAL_DOMAINS.get(platform)

    if expected not in domain:

        raise serializers.ValidationError(

            f"This is not a valid {platform} URL."

        )

    return url