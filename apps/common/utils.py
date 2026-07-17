from django.utils.text import slugify
from django.http import HttpRequest


def generate_slug(value):

    return slugify(value)

def update_instance(instance, validated_data):
    """
    Update a model instance with validated data and save it.
    """
    for field, value in validated_data.items():
        setattr(instance, field, value)

    instance.save()

    return instance



def get_client_ip(
    request: HttpRequest,
) -> str:

    forwarded = request.META.get(
        "HTTP_X_FORWARDED_FOR",
    )

    if forwarded:

        return forwarded.split(",")[0].strip()

    return request.META.get(
        "REMOTE_ADDR",
        "",
    )


def get_user_agent(
    request: HttpRequest,
) -> str:

    return request.META.get(
        "HTTP_USER_AGENT",
        "",
    )