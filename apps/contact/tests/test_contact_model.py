import pytest

from apps.common.tests.factories.contact import (
    ContactFactory,
)


pytestmark = pytest.mark.django_db


def test_create_contact():

    contact = ContactFactory()

    assert contact.pk is not None


def test_reference_created():

    contact = ContactFactory()

    assert contact.reference.startswith(
        "MSG-",
    )


def test_default_status():

    contact = ContactFactory()

    assert contact.status == "new"