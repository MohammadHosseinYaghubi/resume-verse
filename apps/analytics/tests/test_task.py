import pytest

from apps.analytics.models import (
    AnalyticsEventType,
    ResumeAnalytics,
)

from apps.analytics.tasks import (
    record_analytics_event,
)


pytestmark = pytest.mark.django_db


def test_record_event_task(resume):

    record_analytics_event(
        resume.id,
        AnalyticsEventType.RESUME_VIEW,
    )

    analytics = ResumeAnalytics.objects.get(
        resume=resume,
    )

    assert analytics.total_views == 1