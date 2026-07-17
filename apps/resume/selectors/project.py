from django.shortcuts import get_object_or_404

from apps.resume.models import (
    Project,
    ProjectStatus,
)


def project_queryset():

    return (
        Project.objects
        .select_related(
            "resume",
        )
        .prefetch_related(
            "technologies",
            "technologies__category",
        )
    )


def published_projects():

    return (
        project_queryset()
        .filter(
            status=ProjectStatus.PUBLISHED,
        )
    )


def get_project(slug):

    return get_object_or_404(
        published_projects(),
        slug=slug,
    )
    
def my_projects(user):

    return (project_queryset()
        .filter(
            resume__user=user,
        )
    )


def get_my_project(user, project_id):

    return get_object_or_404(
        my_projects(user),
        id=project_id,
    )