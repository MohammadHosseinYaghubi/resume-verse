from django.db import transaction
from apps.common.utils import generate_slug, update_instance
from apps.resume.models import Skill, SkillCategory

@transaction.atomic
def create_category(*, validated_data):

    validated_data["slug"] = generate_slug(validated_data["name"])

    return SkillCategory.objects.create(
        **validated_data
    )
    
@transaction.atomic
def update_category(*, instance, validated_data):
    
    if "name" in validated_data:
        validated_data["slug"] = generate_slug(validated_data["name"])

    for attr, value in validated_data.items():
        setattr(instance, attr, value)

    instance.save()

    return instance

@transaction.atomic
def delete_category(*, instance):
    instance.delete()
    
@transaction.atomic
def create_skill(validated_data):
    validated_data["slug"] = generate_slug(validated_data["name"])

    return Skill.objects.create(**validated_data)

@transaction.atomic
def update_skill(*, skill, validated_data):
    if "name" in validated_data:
        validated_data["slug"] = generate_slug(validated_data["name"])

    return update_instance(skill, validated_data)

@transaction.atomic
def delete_skill(*, instance):
    instance.delete()