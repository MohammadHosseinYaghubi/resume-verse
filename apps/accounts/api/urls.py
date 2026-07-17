from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView
from .routers import router

urlpatterns = [
    path("", include(router.urls)),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),

]