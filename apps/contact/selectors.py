from django.shortcuts import (
    get_object_or_404,
)

from .constants import ContactStatus
from .models import ContactMessage


def contact_queryset():

    return (
        ContactMessage.objects
        .select_related(
            "user",
        )
    )


def get_contact(
    *,
    reference,
):

    return get_object_or_404(
        contact_queryset(),
        reference=reference,
    )


def new_contacts():

    return contact_queryset().filter(
        status=ContactStatus.NEW,
    )


def answered_contacts():

    return contact_queryset().filter(
        status=ContactStatus.ANSWERED,
    )


def closed_contacts():

    return contact_queryset().filter(
        status=ContactStatus.CLOSED,
    )