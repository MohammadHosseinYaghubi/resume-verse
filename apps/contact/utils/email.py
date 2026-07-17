from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from apps.contact.models import ContactMessage


def notify_admin(
    *,
    message: ContactMessage,
):

    EmailMultiAlternatives(

        subject=f"[Contact] {message.subject}",

        message=(
            f"""
Reference:
{message.reference}

Name:
{message.name}

Email:
{message.email}

Message:

{message.message}
"""
        ),

        from_email=settings.DEFAULT_FROM_EMAIL,

        recipient_list=[
            settings.DEFAULT_FROM_EMAIL,
        ],

        fail_silently=False,
    )


def send_auto_reply(
    *,
    message: ContactMessage,
):

    EmailMultiAlternatives(

        subject="We received your message",

        message=(
            f"""
Hello {message.name},

Thank you for contacting us.

Reference:

{message.reference}

We will reply as soon as possible.

ResumeHub Team
"""
        ),

        from_email=settings.DEFAULT_FROM_EMAIL,

        recipient_list=[
            message.email,
        ],

        fail_silently=False,
    )