import pytest

from rest_framework.test import APIClient

from apps.analytics.models import ResumeAnalytics


pytestmark = pytest.mark.django_db


def test_dashboard_analytics(user, resume):

    ResumeAnalytics.objects.create(
        resume=resume,
    )

    client = APIClient()

    client.force_authenticate(
        user=user,
    )

    response = client.get(
        "/api/dashboard/analytics/1/",
    )

    assert response.status_code == 200