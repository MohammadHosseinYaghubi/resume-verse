from rest_framework.routers import SimpleRouter

from apps.accounts.api.views.auth import AuthViewSet

router = SimpleRouter()

router.register(
    "",
    AuthViewSet,
    basename="auth",
)