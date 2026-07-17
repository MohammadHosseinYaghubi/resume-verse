from rest_framework import serializers
from apps.resume.models import Resume, Skill
from .skill import SkillReadSerializer, SkillWriteSerializer
from .project import ProjectReadSerializer
from .social import SocialLinkReadSerializer

class ResumeReadSerializer(serializers.ModelSerializer):

    skills = SkillReadSerializer(
        many=True,
        read_only=True,
    )

    projects = ProjectReadSerializer(
        many=True,
        read_only=True,
    )

    social_links = SocialLinkReadSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Resume

        fields = (
            "id",
            "full_name",
            "slug",
            "title",
            "bio",
            "email",
            "phone",
            "location",
            "experience",
            "education",
            "profile_picture",
            "background_image",
            "skills",
            "projects",
            "social_links",
            "created_at",
            "updated_at",
        )

        read_only_fields = fields


class ResumeWriteSerializer(serializers.ModelSerializer):

    skills = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        many=True,
        required=False,
    )

    class Meta:
        model = Resume

        fields = (
            "full_name",
            "slug",
            "title",
            "bio",
            "email",
            "phone",
            "location",
            "experience",
            "education",
            "profile_picture",
            "background_image",
            "skills",
        )