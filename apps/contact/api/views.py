from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from apps.common.api.responses import success_response
from apps.common.api.viewsets import BaseViewSet
from apps.contact.api.serializers import ContactSerializer, ContactWriteSerializer
from apps.contact.models import ContactMessage
from apps.contact.selectors import get_contact
from apps.contact.services import create_contact_message
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=[
        "Contact",
    ],
)

class ContactViewSet(BaseViewSet):

    queryset = ContactMessage.objects.all()
    lookup_field = "reference"
    serializer_action_classes = {
        "list": ContactSerializer,
        "retrieve": ContactSerializer,
        "create": ContactWriteSerializer,
    }

    def get_permissions(self):
        if self.action == "create":
            permission_classes = (
                AllowAny,
            )

        else:
            permission_classes = (
                IsAdminUser,
            )

        return [
            permission()
            for permission in permission_classes
        ]

    def get_object(self):

        return get_contact(
            reference=self.kwargs[
                "reference"
            ],
        )
        
    @extend_schema(

        summary="Send contact message",

        description="""
            Create a new contact message.

            Guest users must provide:

            - name
            - email
            - subject
            - message

            Authenticated users only send:

            - subject
            - message

            The server automatically fills name and email.
            """,

        request=ContactWriteSerializer,

        responses={
            201: ContactSerializer,
        },

    )

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = create_contact_message(
            validated_data=serializer.validated_data,
            request=request,
        )

        return success_response(
            data=ContactReadSerializer(
                contact,
            ).data,
            message="Message sent successfully.",
            status_code=status.HTTP_201_CREATED,
        )