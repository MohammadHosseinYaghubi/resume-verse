from celery import shared_task

from apps.contact.models import ContactMessage

from apps.contact.utils.email import (
    notify_admin,
    send_auto_reply,
)


@shared_task
def notify_admin_task(
    message_id,
):

    message = ContactMessage.objects.get(
        id=message_id,
    )

    notify_admin(
        message=message,
    )


@shared_task
def auto_reply_task(
    message_id,
):

    message = ContactMessage.objects.get(
        id=message_id,
    )

    send_auto_reply(
        message=message,
    )