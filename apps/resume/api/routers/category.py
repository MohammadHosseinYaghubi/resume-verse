from rest_framework.routers import SimpleRouter

from apps.resume.api.views import (
    SkillCategoryViewSet,
)

router = SimpleRouter()

router.register(
    "skill-categories",
    SkillCategoryViewSet,
    basename="skill-category",
)
