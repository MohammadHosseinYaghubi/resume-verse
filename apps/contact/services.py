from django.db import transaction

from apps.analytics.models import (
    AnalyticsEventType,
)

from apps.analytics.tasks import (
    record_analytics_event,
)

from apps.common.utils import (
    get_client_ip,
    get_user_agent,
)

from apps.contact.models import ContactMessage

from apps.contact.tasks import (
    auto_reply_task,
    notify_admin_task,
)

from apps.contact.utils.rate_limit import (
    check_rate_limit,
)


@transaction.atomic
def create_contact_message(
    *,
    validated_data,
    request,
):

    ip_address = get_client_ip(
        request,
    )

    check_rate_limit(
        ip_address=ip_address,
    )

    if request.user.is_authenticated:

        validated_data["user"] = request.user

        validated_data["name"] = (
            request.user.get_full_name()
            or request.user.username
        )

        validated_data["email"] = (
            request.user.email
        )

    message = ContactMessage.objects.create(

        ip_address=ip_address,

        user_agent=get_user_agent(
            request,
        ),

        **validated_data,

    )

    notify_admin_task.delay(
        message.id,
    )

    auto_reply_task.delay(
        message.id,
    )

    record_analytics_event.delay(

        None,

        AnalyticsEventType.CONTACT,

    )

    return message