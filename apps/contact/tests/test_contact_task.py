import pytest

from unittest.mock import patch

from apps.common.tests.factories.contact import (
    ContactFactory,
)

from apps.contact.tasks import (

    notify_admin_task,

    auto_reply_task,

)


pytestmark = pytest.mark.django_db


@patch(
    "apps.contact.utils.email.notify_admin",
)
def test_notify_admin_task(

    mocked,

):

    contact = ContactFactory()

    notify_admin_task(
        contact.id,
    )

    mocked.assert_called_once()


@patch(
    "apps.contact.utils.email.send_auto_reply",
)
def test_auto_reply_task(

    mocked,

):

    contact = ContactFactory()

    auto_reply_task(
        contact.id,
    )

    mocked.assert_called_once()