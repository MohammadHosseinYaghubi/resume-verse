from django.contrib.auth import get_user_model

from django.contrib.auth.tokens import (
    default_token_generator,
)

from django.db import transaction

from django.utils.http import (
    urlsafe_base64_encode,
    urlsafe_base64_decode,
)

from django.utils.encoding import (
    force_bytes,
    force_str,
)

from django.conf import settings

from apps.notification.services import (
    send_password_reset_notification,
)

User = get_user_model()


def forgot_password(
    *,
    email,
):

    user = User.objects.filter(
        email__iexact=email,
    ).first()

    if not user:

        return

    uid = urlsafe_base64_encode(
        force_bytes(
            user.pk,
        ),
    )

    token = default_token_generator.make_token(
        user,
    )

    reset_url = (

        f"{settings.FRONTEND_URL}"

        f"/reset-password/"

        f"?uid={uid}"

        f"&token={token}"

    )

    send_password_reset_notification(

        user=user,

        reset_url=reset_url,

    )


@transaction.atomic
def reset_password(
    *,
    uid,
    token,
    password,
):

    user = User.objects.get(

        pk=force_str(

            urlsafe_base64_decode(
                uid,
            )

        )

    )

    if not default_token_generator.check_token(
        user,
        token,
    ):

        raise ValueError(
            "Invalid token.",
        )

    user.set_password(
        password,
    )

    user.save()

    return user


@transaction.atomic
def change_password(
    *,
    user,
    old_password,
    new_password,
):

    if not user.check_password(
        old_password,
    ):

        raise ValueError(
            "Old password is incorrect.",
        )

    user.set_password(
        new_password,
    )

    user.save()

    return user