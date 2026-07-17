from rest_framework.routers import SimpleRouter
from apps.resume.api.views import SkillViewSet


router = SimpleRouter()

router.register(
    "skills",
    SkillViewSet,
    basename="skill",
)
