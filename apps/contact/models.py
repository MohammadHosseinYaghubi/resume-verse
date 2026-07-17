from uuid import uuid4
from django.conf import settings
from django.db import models
from apps.common.models import TimeStampedModel
from .constants import ContactStatus
from .managers import ContactManager


def generate_reference():

    return (
        f"MSG-{uuid4().hex[:8].upper()}"
    )


class ContactMessage(
    TimeStampedModel,
):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="contact_messages",
    )

    reference = models.CharField(
        max_length=20,
        unique=True,
        default=generate_reference,
        editable=False,
    )

    name = models.CharField(
        max_length=150,
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=200,
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=ContactStatus.choices,
        default=ContactStatus.NEW,
    )

    ip_address = models.GenericIPAddressField()

    user_agent = models.TextField(
        blank=True,
    )

    objects = ContactManager()

    class Meta:

        ordering = (
            "-created_at",
        )

        indexes = [

            models.Index(
                fields=(
                    "status",
                ),
            ),

            models.Index(
                fields=(
                    "email",
                ),
            ),

            models.Index(
                fields=(
                    "created_at",
                ),
            ),

            models.Index(
                fields=(
                    "reference",
                ),
            ),

        ]

    def __str__(self):

        return (
            f"{self.reference} | "
            f"{self.subject}"
        )