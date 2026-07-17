from django.urls import path

from apps.pdf.api.views import (
    DashboardPDFAPIView,
)

urlpatterns = [

    path(

        "dashboard/pdf/",

        DashboardPDFAPIView.as_view(),

        name="dashboard-pdf",

    ),

]