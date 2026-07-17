from rest_framework.routers import SimpleRouter
from .views import DashboardAnalyticsViewSet

router = SimpleRouter()

router.register(
    "dashboard/analytics",
    DashboardAnalyticsViewSet,
    basename="dashboard-analytics",
)