import factory

from apps.analytics.models import ResumeAnalytics, AnalyticsEvent, AnalyticsEventType

from .resume import ResumeFactory


class ResumeAnalyticsFactory(
    factory.django.DjangoModelFactory,
):

    class Meta:

        model = ResumeAnalytics

    resume = factory.SubFactory(
        ResumeFactory,
    )

    total_views = 0

    total_downloads = 0

    total_contacts = 0
    

class AnalyticsEventFactory(
    factory.django.DjangoModelFactory,
):

    class Meta:

        model = AnalyticsEvent

    resume = factory.SubFactory(
        ResumeFactory,
    )

    event = AnalyticsEventType.RESUME_VIEW

    ip_address = "127.0.0.1"

    user_agent = "pytest"