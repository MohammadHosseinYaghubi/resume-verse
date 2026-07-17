from django.db import transaction
from apps.common.cache import (
    cache_delete,
    resume_key,
)
from apps.resume.models import Resume


@transaction.atomic
def create_resume(*, validated_data):
    """
    Create Resume with related skills.
    """

    skills = validated_data.pop(
        "skills",
        [],
    )

    resume = Resume.objects.create(
        **validated_data
    )

    resume.skills.set(skills)

    return resume


@transaction.atomic
def update_resume(*, resume, validated_data):
    """
    Update Resume.
    """

    skills = validated_data.pop(
        "skills",
        None,
    )

    for attr, value in validated_data.items():
        setattr(resume, attr, value)

    resume.save()

    if skills is not None:
        resume.skills.set(skills)
        
    cache_delete(
        resume_key(
            resume.slug,
        )
    )
    
    return resume