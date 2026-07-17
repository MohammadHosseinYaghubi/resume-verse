from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from apps.common.api.viewsets import BaseViewSet

from apps.resume.api.serializers.project import (
    ProjectListSerializer,
    ProjectReadSerializer,
    ProjectWriteSerializer,
)

from apps.resume.selectors.project import my_projects
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=[
        "DashboardProject",
    ],
)
class DashboardProjectViewSet(
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.CreateModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                BaseViewSet,
                            ):

    permission_classes = (IsAuthenticated)
    lookup_field = "id"

    def get_queryset(self):
        return my_projects(self.request.user)

    def get_serializer_class(self):

        if self.action == "list":
            return ProjectListSerializer

        if self.action == "retrieve":
            return ProjectReadSerializer

        return ProjectWriteSerializer

    def perform_create(self, serializer):
        serializer.save(resume=self.request.user.resume)

    def perform_update(self, serializer):
        serializer.save()