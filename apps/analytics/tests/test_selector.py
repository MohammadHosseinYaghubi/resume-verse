import pytest

from apps.analytics.models import ResumeAnalytics

from apps.analytics.selectors import (
    analytics_queryset,
    get_resume_analytics,
)


pytestmark = pytest.mark.django_db


def test_analytics_queryset(resume):

    ResumeAnalytics.objects.create(
        resume=resume,
    )

    assert analytics_queryset().count() == 1


def test_get_resume_analytics(resume):

    analytics = ResumeAnalytics.objects.create(
        resume=resume,
    )

    result = get_resume_analytics(
        resume=resume,
    )

    assert result == analytics