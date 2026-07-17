from django.shortcuts import get_object_or_404

from .models import (
    ResumeAnalytics,
    AnalyticsEvent,
)


def analytics_queryset():

    return ResumeAnalytics.objects.select_related(
        "resume",
    )


def event_queryset():

    return AnalyticsEvent.objects.select_related(
        "resume",
    )


def get_resume_analytics(
    *,
    resume,
):

    return get_object_or_404(
        analytics_queryset(),
        resume=resume,
    )


def resume_events(
    *,
    resume,
):

    return event_queryset().filter(
        resume=resume,
    )