from apps.common.api.permissions import (
    IsAdminOrReadOnly,
)

from apps.common.api.viewsets import (
    BaseViewSet,
)

from apps.resume.api.filters.skill import (
    CategoryFilter,
)

from apps.resume.api.serializers.skill import (
    SkillCategoryListSerializer,
    SkillCategoryReadSerializer,
    SkillCategoryWriteSerializer,
)

from apps.resume.selectors.skill import (
    category_queryset,
)

from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=[
        "Category",
    ],
)
class SkillCategoryViewSet(BaseViewSet):

    queryset = category_queryset()

    permission_classes = (
        IsAdminOrReadOnly,
    )

    filterset_class = CategoryFilter

    search_fields = (
        "name",
        "slug",
    )

    ordering_fields = (
        "name",
        "created_at",
    )

    serializer_action_classes = {

        "list": SkillCategoryListSerializer,

        "retrieve": SkillCategoryReadSerializer,

        "create": SkillCategoryWriteSerializer,

        "update": SkillCategoryWriteSerializer,

        "partial_update": SkillCategoryWriteSerializer,
    }