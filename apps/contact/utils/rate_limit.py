from datetime import timedelta

from django.utils import timezone

from rest_framework.exceptions import Throttled

from apps.contact.models import ContactMessage


RATE_LIMIT = 5

WINDOW = timedelta(
    minutes=10,
)


def check_rate_limit(
    *,
    ip_address,
):

    since = timezone.now() - WINDOW

    count = ContactMessage.objects.filter(
        ip_address=ip_address,
        created_at__gte=since,
    ).count()

    if count >= RATE_LIMIT:

        raise Throttled(
            detail=(
                "Too many contact requests. "
                "Please try again later."
            ),
        )