from django.db import transaction
from .models import (
    AnalyticsEvent,
    AnalyticsEventType,
    ResumeAnalytics,
)


from .models import (
    AnalyticsEvent,
    ResumeAnalytics,
)


@transaction.atomic
def record_event(
    *,
    event_type,
    resume=None,
    user=None,
):

    AnalyticsEvent.objects.create(
        resume=resume,
        user=user,
        event=event_type,
    )

    if resume is None:
        return
    analytics, _ = (
        ResumeAnalytics.objects.get_or_create(
            resume=resume,
        )
    )

    if event_type == AnalyticsEventType.RESUME_VIEW:
        analytics.total_views += 1

    elif event_type == AnalyticsEventType.PDF_DOWNLOAD:
        analytics.total_downloads += 1

    elif event_type == AnalyticsEventType.CONTACT:
        analytics.total_contacts += 1

    analytics.save(
        update_fields=[
            "total_views",
            "total_downloads",
            "total_contacts",
        ],
    )