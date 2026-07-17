from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets

class BaseViewSet(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet,):
    """
    Base ViewSet for all APIs.
    """

    lookup_field = "id"

    lookup_url_kwarg = "id"

    serializer_class = None

    serializer_action_classes = {}

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    search_fields = ()

    ordering_fields = ()

    ordering = ("-created_at",)

    def get_serializer_class(self):

        return self.serializer_action_classes.get(
            self.action,
            self.serializer_class,
        )