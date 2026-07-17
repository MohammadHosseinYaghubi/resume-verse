from rest_framework.routers import SimpleRouter

from apps.resume.api.views.resume import (
    ResumeViewSet,
)

router = SimpleRouter()

router.register(
    "resumes",
    ResumeViewSet,
    basename="resume",
)
