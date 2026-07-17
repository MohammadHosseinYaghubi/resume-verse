from django.shortcuts import get_object_or_404
from apps.resume.models import Skill, SkillCategory


def category_queryset():
    return (SkillCategory.objects.all().order_by("name"))


def skill_queryset():
    return (Skill.objects.select_related("category").order_by("name"))


def get_category(category_id):
    return get_object_or_404(category_queryset(), id=category_id)


def get_skill(skill_id):
    return get_object_or_404(skill_queryset(), id=skill_id)


def category_skills(category_id):
    return (skill_queryset().filter(category_id=category_id))


def search_skills(search):
    return (skill_queryset().filter(name__icontains=search))