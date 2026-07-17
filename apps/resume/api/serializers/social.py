from rest_framework import serializers

from apps.resume.models import (
    Resume,
    SocialLink,
)

from apps.resume.services.social import (
    create_social,
    update_social,
)

from apps.resume.api.serializers.validators import  validate_social_url

from .base import (
    BaseReadSerializer,
    BaseWriteSerializer,
)


class SocialLinkListSerializer(BaseReadSerializer):

    class Meta:

        model = SocialLink

        fields = (
            "id",
            "platform",
            "url",
        )

        read_only_fields = fields


class SocialLinkReadSerializer(BaseReadSerializer):

    class Meta:

        model = SocialLink

        fields = (
            "id",
            "resume",
            "platform",
            "url",
            "display_order",
            "created_at",
            "updated_at",
        )

        read_only_fields = fields


class SocialLinkWriteSerializer(BaseWriteSerializer):

    resume = serializers.PrimaryKeyRelatedField(
        queryset=Resume.objects.all(),
    )

    class Meta:
        model = SocialLink

        fields = (
            "platform",
            "url",
            "display_order",
        )

    def validate(self, attrs):

        validate_social_url(
            attrs["platform"],
            attrs["url"],
        )

        return attrs

    def create(self, validated_data):
        resume = validated_data.pop("resume")

        return create_social(
            resume=resume,
            validated_data=validated_data,
        )

    def update(self, instance, validated_data):
        return update_social(
            instance,
            validated_data,
        )