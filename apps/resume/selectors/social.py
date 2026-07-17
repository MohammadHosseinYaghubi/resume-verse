from django.shortcuts import get_object_or_404
from apps.resume.models import SocialLink

def social_queryset():

    return (
        SocialLink.objects
        .select_related(
            "resume",
        )
    )

def get_social(social_id):

    return get_object_or_404(
        social_queryset(),
        id=social_id,
    )
    
def my_social_links(user):

    return (social_queryset()
        .filter(
            resume__user=user,
        )
    )


def get_my_social(user, social_id):

    return get_object_or_404(
        my_social_links(user),
        id=social_id,
    )