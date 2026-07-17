from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from apps.common.api.viewsets import BaseViewSet

from apps.resume.models import Project

from apps.resume.selectors.project import (
    project_queryset,
)

from apps.resume.api.serializers.project import (
    ProjectListSerializer,
    ProjectReadSerializer,
    ProjectWriteSerializer,
)

from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=[
        "Projects",
    ],
)
class ProjectViewSet(BaseViewSet):

    queryset = project_queryset()

    lookup_field = "slug"

    search_fields = (
        "title",
        "description",
    )

    ordering_fields = (
        "display_order",
        "published_at",
        "created_at",
    )

    serializer_action_classes = {

        "list": ProjectListSerializer,

        "retrieve": ProjectReadSerializer,

        "create": ProjectWriteSerializer,

        "update": ProjectWriteSerializer,

        "partial_update": ProjectWriteSerializer,
    }

    def get_permissions(self):

        if self.action in (
            "list",
            "retrieve",
        ):
            return [
                AllowAny(),
            ]

        return [
            IsAuthenticated(),
        ]