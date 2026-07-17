import pytest

from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db


def test_guest_create_contact():

    client = APIClient()

    response = client.post(

        "/api/contact/contacts/",

        {

            "name": "Ali",

            "email": "ali@test.com",

            "subject": "Test Subject",

            "message": "This is a test contact message.",

        },

        format="json",

    )

    assert response.status_code == 201