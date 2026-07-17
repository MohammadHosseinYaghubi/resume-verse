from apps.common.api.permissions import (
    IsAdminOrReadOnly,
)

from apps.common.api.viewsets import (
    BaseViewSet,
)

from apps.resume.api.filters.social import (
    SocialFilter,
)

from apps.resume.api.serializers.social import (
    SocialLinkListSerializer,
    SocialLinkReadSerializer,
    SocialLinkWriteSerializer,
)

from apps.resume.selectors.social import (
    social_queryset,
)

from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=[
        "Social Links",
    ],
)
class SocialLinkViewSet(BaseViewSet):

    permission_classes = (
        IsAdminOrReadOnly,
    )

    filterset_class = SocialFilter

    search_fields = (
        "platform",
    )

    ordering_fields = (
        "display_order",
        "created_at",
    )

    serializer_action_classes = {

        "list": SocialLinkListSerializer,

        "retrieve": SocialLinkReadSerializer,

        "create": SocialLinkWriteSerializer,

        "update": SocialLinkWriteSerializer,

        "partial_update": SocialLinkWriteSerializer,
    }

    def get_queryset(self):

        return social_queryset()