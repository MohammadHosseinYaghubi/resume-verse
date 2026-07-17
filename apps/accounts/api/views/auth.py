from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.common.api.viewsets import BaseViewSet

from apps.accounts.api.serializers.login import LoginSerializer
from apps.accounts.api.serializers.logout import LogoutSerializer
from apps.accounts.api.serializers.me import MeSerializer

from apps.accounts.services.auth import login_user, logout_user
from apps.common.api.throttles import LoginRateThrottle
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=[
        "Authentication",
    ],
)
class AuthViewSet(BaseViewSet):
    """
    Authentication endpoints.
    """

    queryset = None
    
    serializer_action_classes = {
        "login": LoginSerializer,
        "logout": LogoutSerializer,
        "me": MeSerializer,
    }
    
    @extend_schema(
        summary="Login",
        description="Authenticate user and return JWT tokens.",
    )
    @action(
        detail=False,
        methods=["post"],
        permission_classes=[AllowAny],
        throttle_classes=[LoginRateThrottle],
        url_path="login",
    )
    def login(self, request):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        data = login_user(
            serializer.validated_data["user"],
        )

        return Response(
            data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Logout",
    )
    @action(
        detail=False,
        methods=["post"],
        permission_classes=[IsAuthenticated],
        url_path="logout",
    )
    def logout(self, request):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        logout_user(
            serializer.validated_data["refresh"],
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )

    @extend_schema(
        summary="Me",
    )
    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsAuthenticated],
        url_path="me",
    )
    def me(self, request):

        serializer = self.get_serializer( request.user)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
        