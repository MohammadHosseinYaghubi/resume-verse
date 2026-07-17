from rest_framework.routers import SimpleRouter

from apps.resume.api.views.project import (
    ProjectViewSet,
)

router = SimpleRouter()

router.register(
    "projects",
    ProjectViewSet,
    basename="project",
)
