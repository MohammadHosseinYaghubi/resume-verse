from rest_framework import mixins
from rest_framework import viewsets

from django_filters.rest_framework import (
    DjangoFilterBackend,
)

from rest_framework.filters import (
    OrderingFilter,
    SearchFilter,
)

from apps.common.api.permissions import (
    IsAdminOrReadOnly,
)

from apps.resume.models import (
    Skill,
)

from apps.resume.selectors.skill import (
    skill_queryset,
)

from apps.resume.api.serializers.skill import (
    SkillListSerializer,
    SkillReadSerializer,
    SkillWriteSerializer,
)

from apps.resume.api.filters.skill import SkillFilter
from apps.common.api.viewsets import BaseViewSet
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=[
        "Skills",
    ],
)
class SkillViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   BaseViewSet,
                  ):

    permission_classes = (IsAdminOrReadOnly)
    
    search_fields = (
        "name",
    )
    
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )
    
    ordering_fields = (
        "name",
        "created_at",
    )
    
    def get_queryset(self):
        return skill_queryset()
    
    def get_serializer_class(self):
        if self.action == "list":
            return SkillListSerializer

        if self.action == "retrieve":
            return SkillReadSerializer

        return SkillWriteSerializer
    
    
filterset_class = SkillFilter