from django.db import transaction

from apps.common.utils import update_instance
from apps.resume.models import SocialLink


@transaction.atomic
def create_social(validated_data):

    return SocialLink.objects.create(
        **validated_data,
    )

@transaction.atomic
def update_social(instance, validated_data):

    return update_instance(
        instance,
        validated_data,
    )