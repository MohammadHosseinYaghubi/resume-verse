from django.db import transaction

from apps.resume.models import Project


@transaction.atomic
def create_project(*, resume,validated_data):

    technologies = validated_data.pop("technologies", [])
    project = Project.objects.create(
        resume=resume,
        **validated_data,
    )

    project.technologies.set(technologies)

    return project


@transaction.atomic
def update_project(*, project, validated_data):

    technologies = validated_data.pop(
        "technologies",
        None,
    )

    for attr, value in validated_data.items():
        setattr(
            project,
            attr,
            value,
        )

    project.save()

    if technologies is not None:

        project.technologies.set(
            technologies,
        )

    return project