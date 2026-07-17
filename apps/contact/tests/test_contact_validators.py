import pytest

from rest_framework.serializers import ValidationError

from apps.contact.validators import (

    validate_name,

    validate_subject,

    validate_message,

)


def test_validate_name():

    assert validate_name(
        "Ali",
    ) == "Ali"


def test_invalid_name():

    with pytest.raises(
        ValidationError,
    ):

        validate_name(
            "A",
        )


def test_invalid_subject():

    with pytest.raises(
        ValidationError,
    ):

        validate_subject(
            "abc",
        )


def test_invalid_message():

    with pytest.raises(
        ValidationError,
    ):

        validate_message(
            "short",
        )