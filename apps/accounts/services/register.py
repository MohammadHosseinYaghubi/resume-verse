from django.contrib.auth import (
    get_user_model,
)

from django.db import transaction

from apps.notification.services import (
    send_welcome_notification,
)

User = get_user_model()


@transaction.atomic
def register_user(
    *,
    validated_data,
):

    validated_data.pop(
        "password_confirm",
    )

    password = validated_data.pop(
        "password",
    )

    user = User.objects.create_user(

        password=password,

        **validated_data,

    )

    send_welcome_notification(
        user,
    )

    return user