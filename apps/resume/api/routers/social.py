from rest_framework.routers import SimpleRouter

from apps.resume.api.views.social import (
    SocialLinkViewSet,
)

router = SimpleRouter()

router.register(
    "social-links",
    SocialLinkViewSet,
    basename="social",
)
