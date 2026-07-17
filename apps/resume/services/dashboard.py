from django.db import transaction

from apps.common.utils import update_instance


@transaction.atomic
def update_my_resume(*,
    resume,
    validated_data,
):

    return update_instance(
        resume,
        validated_data,
    )
    
