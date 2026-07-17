from celery import shared_task

from django.contrib.auth import get_user_model

from apps.analytics.services import (
    record_event,
)

from apps.resume.models import Resume

from .models import (
    AnalyticsEventType,
)


User = get_user_model()


@shared_task(
    name="analytics.record_event",
)
def record_event_task(
    *,
    event_type,
    resume_id=None,
    user_id=None,
):

    resume = None
    user = None

    if resume_id is not None:

        resume = Resume.objects.filter(
            id=resume_id,
        ).first()

    if user_id is not None:

        user = User.objects.filter(
            id=user_id,
        ).first()

    record_event(
        event_type=event_type,
        resume=resume,
        user=user,
    )