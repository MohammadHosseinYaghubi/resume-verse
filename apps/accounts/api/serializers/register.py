from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.accounts.validators import (
    validate_password,
)

User = get_user_model()


class RegisterSerializer(
    serializers.ModelSerializer,
):

    password = serializers.CharField(
        write_only=True,
        validators=[
            validate_password,
        ],
        style={
            "input_type": "password",
        },
    )

    password_confirm = serializers.CharField(
        write_only=True,
        style={
            "input_type": "password",
        },
    )

    class Meta:

        model = User

        fields = (

            "username",

            "first_name",

            "last_name",

            "email",

            "password",

            "password_confirm",

        )

    def validate_email(
        self,
        value,
    ):

        if User.objects.filter(
            email__iexact=value,
        ).exists():

            raise serializers.ValidationError(
                "Email already exists.",
            )

        return value

    def validate(
        self,
        attrs,
    ):

        if (
            attrs["password"]
            != attrs["password_confirm"]
        ):

            raise serializers.ValidationError(

                {

                    "password_confirm":
                        "Passwords do not match."

                }

            )

        return attrs