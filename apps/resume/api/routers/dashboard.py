from rest_framework.routers import SimpleRouter

from apps.resume.api.views.dashboard.resume import (
    DashboardResumeViewSet,
)

router = SimpleRouter()

router.register(
    "dashboard/projects",
    DashboardProjectViewSet,
    basename="dashboard-project",
)

router.register(
    "dashboard/socials",
    DashboardSocialViewSet,
    basename="dashboard-social",
)

