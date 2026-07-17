from rest_framework import serializers

from apps.contact.models import (
    ContactMessage,
)

from apps.contact.validators import (
    validate_message,
    validate_name,
    validate_subject,
)


class ContactWriteSerializer(
    serializers.ModelSerializer,
):

    class Meta:

        model = ContactMessage

        fields = (

            "name",

            "email",

            "subject",

            "message",

        )

    validate_name = staticmethod(
        validate_name,
    )

    validate_subject = staticmethod(
        validate_subject,
    )

    validate_message = staticmethod(
        validate_message,
    )

    def validate(
        self,
        attrs,
    ):

        request = self.context[
            "request"
        ]

        if request.user.is_authenticated:

            attrs.pop(
                "name",
                None,
            )

            attrs.pop(
                "email",
                None,
            )

        else:

            if not attrs.get(
                "name",
            ):

                raise serializers.ValidationError(
                    {
                        "name": "This field is required.",
                    },
                )

            if not attrs.get(
                "email",
            ):

                raise serializers.ValidationError(
                    {
                        "email": "This field is required.",
                    },
                )

        return attrs


class ContactSerializer(
    serializers.ModelSerializer,
):

    class Meta:

        model = ContactMessage

        fields = (

            "reference",

            "status",

            "created_at",

        )

        read_only_fields = fields


class ContactAdminSerializer(
    serializers.ModelSerializer,
):

    class Meta:

        model = ContactMessage

        fields = "__all__"

        read_only_fields = (

            "reference",

            "created_at",

            "updated_at",

        )