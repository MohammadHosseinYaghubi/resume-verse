import pytest

from django.test import RequestFactory

from django.contrib.auth.models import AnonymousUser

from apps.contact.services import (
    create_contact_message,
)


pytestmark = pytest.mark.django_db


def test_create_contact_message():

    request = RequestFactory().post(
        "/contact/",
    )

    request.user = AnonymousUser()

    request.META["REMOTE_ADDR"] = "127.0.0.1"

    request.META["HTTP_USER_AGENT"] = "pytest"

    contact = create_contact_message(

        validated_data={

            "name": "Ali",

            "email": "ali@test.com",

            "subject": "Hello",

            "message": "This is a test message.",

        },

        request=request,

    )

    assert contact.pk is not None