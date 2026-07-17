from django.urls import include, path

from .routers.project import router as project_router
from .routers.resume import router as resume_router
from .routers.skill import router as skill_router
from .routers.social import router as social_router
from .routers.category import router as category_router
from apps.resume.api.routers.dashboard import (
    router as dashboard_router,
)
from apps.resume.api.views.dashboard.resume import (
    DashboardResumeAPIView,
)

# from apps.resume.api.views.dashboard.profile import (
#     DashboardProfileAPIView,
# )

urlpatterns = [

    path(
        "",
        include(project_router.urls),
    ),

    path(
        "",
        include(skill_router.urls),
    ),

    path(
        "",
        include(category_router.urls),
    ),

    path(
        "",
        include(social_router.urls),
    ),

    path(
        "",
        include(resume_router.urls),
    ),
    
    path(
        "dashboard/resume/",
        DashboardResumeAPIView.as_view(),
        name="dashboard-resume",
    ),

    # path(
    #     "dashboard/profile/",
    #     DashboardProfileAPIView.as_view(),
    #     name="dashboard-profile",
    # ),
    
    path(
        "",
        include(dashboard_router.urls),
    ),
    
    
    
]