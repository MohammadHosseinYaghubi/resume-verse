import pytest

from apps.analytics.models import (
    AnalyticsEvent,
    ResumeAnalytics,
)


pytestmark = pytest.mark.django_db


def test_create_resume_analytics(resume):

    analytics = ResumeAnalytics.objects.create(
        resume=resume,
    )

    assert analytics.resume == resume
    assert analytics.total_views == 0
    assert analytics.total_downloads == 0
    assert analytics.total_contacts == 0


def test_create_event(resume):

    event = AnalyticsEvent.objects.create(
        resume=resume,
        event="resume_view",
    )

    assert event.resume == resume
    assert event.event == "resume_view"