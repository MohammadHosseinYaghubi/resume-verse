from rest_framework import serializers
from apps.resume.models import Skill, SkillCategory
from apps.resume.services.skill import (
    create_skill,
    update_skill,
    create_category,
    update_category,
)
from .base import BaseReadSerializer, BaseWriteSerializer
from .validators import validate_name, validate_slug

class SkillCategoryListSerializer(BaseReadSerializer):

    class Meta:
        model = SkillCategory

        fields = (
            "id",
            "name",
            "slug",
        )

class SkillCategoryReadSerializer(BaseReadSerializer):

    skills_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = SkillCategory

        fields = (
            "id",
            "name",
            "slug",
            "skills_count",
            "created_at",
            "updated_at",
        )

class SkillCategoryWriteSerializer(BaseWriteSerializer):

    validate_name = staticmethod(validate_name)

    class Meta:
        model = SkillCategory

        fields = (
            "name",
        )
        
    def create(self, validated_data):
        return create_category(validated_data)
    
    def update(self, instance, validated_data):
        return update_category(instance, validated_data)

class SkillReadSerializer(BaseReadSerializer):
    
    category = SkillCategoryListSerializer()

    class Meta:
        model = Skill
        fields = (
            "id",
            "name",
            "slug",
            "category",
            "created_at",
            "updated_at",
        )
        
class SkillListSerializer(BaseReadSerializer):
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Skill

        fields = (
            "id",
            "name",
            "slug",
            "category",
        )
        read_only_fields = fields
        
class SkillWriteSerializer(BaseWriteSerializer):

    category = serializers.PrimaryKeyRelatedField(
        queryset=SkillCategory.objects.all(),
    )
    
    validate_name = staticmethod(validate_name)

    class Meta:
        model = Skill

        fields = (
            "name",
            "category",
        )
    
    def create(self, validated_data):
        return create_skill(validated_data)
    
    def update(self, instance, validated_data):
        return update_skill(instance, validated_data)