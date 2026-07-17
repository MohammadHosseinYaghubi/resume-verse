from django.shortcuts import get_object_or_404
from apps.resume.models import Resume
from apps.common.cache import cache_get, cache_set, resume_key


def resume_queryset():
    return Resume.objects.detail()


def get_resume(slug):

    key = resume_key(slug)
    resume = cache_get(key)

    if resume is not None:
        return resume

    resume = get_object_or_404(resume_queryset(), slug=slug)
    cache_set(key, resume)

    return resume


def my_resume(user):
    return get_object_or_404(Resume.objects.select_related("user"),
                            user=user
                            )