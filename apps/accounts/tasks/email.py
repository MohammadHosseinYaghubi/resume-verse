from celery import shared_task


@shared_task(
    name="accounts.email.send_welcome_email",
)
def send_welcome_email(
    user_id,
):

    """
    Send welcome email.

    Implementation will be added later.
    """

    return user_id