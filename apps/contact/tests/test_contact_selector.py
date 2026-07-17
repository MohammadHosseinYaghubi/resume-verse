import pytest

from apps.contact.selectors import (
    get_contact,
)

from apps.common.tests.factories.contact import (
    ContactFactory,
)


pytestmark = pytest.mark.django_db


def test_get_contact():

    contact = ContactFactory()

    result = get_contact(
        reference=contact.reference,
    )

    assert result.id == contact.id