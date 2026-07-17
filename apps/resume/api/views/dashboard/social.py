from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from apps.common.api.viewsets import BaseViewSet

from apps.resume.api.serializers.social import (
    SocialLinkListSerializer,
    SocialLinkReadSerializer,
    SocialLinkWriteSerializer,
)

from apps.resume.selectors.social import my_social_links

from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=[
        "DashboardCategory",
    ],
)
class DashboardSocialViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.CreateModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             BaseViewSet
                            ):

    permission_classes = (IsAuthenticated)
    lookup_field = "id"

    def get_queryset(self):
        return my_social_links(self.request.user)

    def get_serializer_class(self):

        if self.action == "list":
            return SocialLinkListSerializer

        if self.action == "retrieve":
            return SocialLinkReadSerializer

        return SocialLinkWriteSerializer

    def perform_create(self, serializer):
        serializer.save(resume=self.request.user.resume)

    def perform_update(self, serializer):
        serializer.save()