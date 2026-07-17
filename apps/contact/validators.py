from rest_framework import serializers


def validate_subject(
    value,
):

    value = value.strip()

    if len(value) < 5:

        raise serializers.ValidationError(
            "Subject must contain at least 5 characters.",
        )

    return value


def validate_message(
    value,
):

    value = value.strip()

    if len(value) < 20:

        raise serializers.ValidationError(
            "Message must contain at least 20 characters.",
        )

    return value


def validate_name(
    value,
):

    value = value.strip()

    if len(value) < 2:

        raise serializers.ValidationError(
            "Invalid name.",
        )

    return value