import django_filters

from apps.resume.models import (
    SocialLink,
    SocialPlatform,
)


class SocialFilter(django_filters.FilterSet):

    platform = django_filters.ChoiceFilter(
        choices=SocialPlatform.choices,
    )

    resume = django_filters.UUIDFilter(
        field_name="resume__id",
    )

    class Meta:

        model = SocialLink

        fields = (
            "platform",
            "resume",
        )