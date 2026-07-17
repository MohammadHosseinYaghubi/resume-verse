from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(
    admin.ModelAdmin,
):

    list_display = (

        "reference",

        "name",

        "email",

        "status",

        "created_at",

    )

    list_filter = (

        "status",

        "created_at",

    )

    search_fields = (

        "reference",

        "name",

        "email",

        "subject",

    )

    readonly_fields = (

        "reference",

        "ip_address",

        "user_agent",

        "created_at",

        "updated_at",

    )

    ordering = (

        "-created_at",

    )