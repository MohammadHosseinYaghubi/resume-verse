import pytest

from apps.analytics.models import (
    AnalyticsEventType,
    ResumeAnalytics,
)

from apps.analytics.services import (
    record_event,
)


pytestmark = pytest.mark.django_db


def test_record_resume_view(resume):

    record_event(
        resume=resume,
        event=AnalyticsEventType.RESUME_VIEW,
    )

    analytics = ResumeAnalytics.objects.get(
        resume=resume,
    )

    assert analytics.total_views == 1


def test_record_pdf_download(resume):

    record_event(
        resume=resume,
        event=AnalyticsEventType.PDF_DOWNLOAD,
    )

    analytics = ResumeAnalytics.objects.get(
        resume=resume,
    )

    assert analytics.total_downloads == 1


def test_record_contact(resume):

    record_event(
        resume=resume,
        event=AnalyticsEventType.CONTACT,
    )

    analytics = ResumeAnalytics.objects.get(
        resume=resume,
    )

    assert analytics.total_contacts == 1