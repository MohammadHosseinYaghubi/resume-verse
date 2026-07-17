from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from apps.common.api.responses import success_response
from apps.common.api.viewsets import BaseViewSet
from apps.resume.models import Resume

from apps.resume.selectors.resume import (
    get_resume,
)

from apps.resume.services.resume import (
    create_resume,
    update_resume,
)

from apps.resume.api.serializers.resume import (
    ResumeReadSerializer,
    ResumeWriteSerializer,
)

from drf_spectacular.utils import extend_schema

from rest_framework.response import Response

from apps.analytics.models import AnalyticsEventType
from apps.analytics.tasks import record_analytics_event


@extend_schema(
    tags=[
        "Resume",
    ],
)
class ResumeViewSet(BaseViewSet):
    """
    Resume API.
    """

    queryset = Resume.objects.detail()
    lookup_field = "slug"

    serializer_action_classes = {
        "list": ResumeReadSerializer,
        "retrieve": ResumeReadSerializer,
        "create": ResumeWriteSerializer,
        "update": ResumeWriteSerializer,
        "partial_update": ResumeWriteSerializer,
    }

    def get_permissions(self):

        if self.action in (
            "list",
            "retrieve",
        ):
            permission_classes = [AllowAny]

        else:
            permission_classes = [IsAuthenticated]

        return [
            permission()
            for permission in permission_classes
        ]

    def get_object(self):

        return get_resume(
            self.kwargs["slug"],
        )

    def perform_create(
        self,
        serializer,
    ):

        self.instance = create_resume(
            serializer.validated_data,
        )

    def perform_update(
        self,
        serializer,
    ):

        self.instance = update_resume(
            resume=self.get_object(),
            validated_data=serializer.validated_data,
        )

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        self.perform_create(
            serializer,
        )

        return success_response(
            data=ResumeReadSerializer(
                self.instance
            ).data,
            message="Resume created successfully.",
            status_code=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data,
            partial=kwargs.get(
                "partial",
                False,
            ),
        )

        serializer.is_valid(
            raise_exception=True,
        )

        self.perform_update(
            serializer,
        )

        return success_response(
            data=ResumeReadSerializer(
                self.instance
            ).data,
            message="Resume updated successfully.",
        )
        
    def retrieve(self, request, *args, **kwargs,):

        resume = self.get_object()
        record_analytics_event.delay(
            resume.id,
            AnalyticsEventType.RESUME_VIEW,
            request.META.get("REMOTE_ADDR"),
            request.META.get("HTTP_USER_AGENT", ""),
        )

        serializer = ResumeReadSerializer(resume)

        return success_response(data=serializer.data)