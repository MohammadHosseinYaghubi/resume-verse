from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from apps.resume.api.serializers.resume import (
    ResumeReadSerializer,
    ResumeWriteSerializer,
)

from apps.resume.selectors.resume import (
    my_resume,
)

from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=[
        "DashboardResume",
    ],
)
class DashboardResumeAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericAPIView,
):

    permission_classes = (
        IsAuthenticated,
    )

    def get_object(self):

        return my_resume(
            self.request.user,
        )

    def get_serializer_class(self):

        if self.request.method == "GET":
            return ResumeReadSerializer

        return ResumeWriteSerializer

    def get(self, request):

        return self.retrieve(
            request,
        )

    def patch(self, request):

        return self.partial_update(
            request,
        )