from rest_framework import serializers

from apps.accounts.validators import (
    validate_password,
)


class ChangePasswordSerializer(
    serializers.Serializer,
):

    old_password = serializers.CharField(
        write_only=True,
    )

    new_password = serializers.CharField(
        write_only=True,
        validators=[
            validate_password,
        ],
    )


class ForgotPasswordSerializer(
    serializers.Serializer,
):

    email = serializers.EmailField()


class ResetPasswordSerializer(
    serializers.Serializer,
):

    token = serializers.CharField()

    password = serializers.CharField(
        write_only=True,
        validators=[
            validate_password,
        ],
    )

    password_confirm = serializers.CharField(
        write_only=True,
    )

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