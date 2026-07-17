from rest_framework import serializers

from apps.resume.models import Project, Skill
from apps.resume.services.project import create_project, update_project

from .base import BaseReadSerializer, BaseWriteSerializer
from .skill import SkillListSerializer
from .validators import validate_name, validate_slug

# ---------------------------------------------------------
# List
# ---------------------------------------------------------

class ProjectListSerializer(BaseReadSerializer):

    class Meta:
        model = Project

        fields = (
            "id",
            "title",
            "slug",
            "image",
        )

        read_only_fields = fields


# ---------------------------------------------------------
# Detail
# ---------------------------------------------------------

class ProjectReadSerializer(BaseReadSerializer):

    technologies = SkillListSerializer(
        many=True,
        read_only=True,
    )

    embed_url = serializers.ReadOnlyField()

    class Meta:
        model = Project

        fields = (
            "id",
            "resume",
            "title",
            "slug",
            "description",
            "technologies",
            "project_url",
            "video_url",
            "embed_url",
            "image",
            "status",
            "published_at",
            "display_order",
            "created_at",
            "updated_at",
        )

        read_only_fields = fields


# ---------------------------------------------------------
# Write
# ---------------------------------------------------------

class ProjectWriteSerializer(BaseWriteSerializer):

    technologies = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        many=True,
        required=False,
    )

    validate_name = staticmethod(validate_name)
    validate_slug = staticmethod(validate_slug)

    class Meta:
        model = Project

        fields = (
            "title",
            "slug",
            "description",
            "technologies",
            "project_url",
            "video_url",
            "image",
            "status",
            "published_at",
            "display_order",
        )

    def create(self, validated_data):
        resume = validated_data.pop("resume")

        return create_project(
            resume=resume,
            validated_data=validated_data,
        )

    def update(self, instance, validated_data):
        return update_project(
            project=instance,
            validated_data=validated_data,
        )