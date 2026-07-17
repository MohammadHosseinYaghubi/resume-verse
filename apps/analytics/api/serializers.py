from rest_framework import serializers
from apps.analytics.models import ResumeAnalytics


class ResumeAnalyticsSerializer(
    serializers.ModelSerializer,
):

    class Meta:

        model = ResumeAnalytics

        fields = (
            "total_views",
            "total_downloads",
            "total_contacts",
            "last_event",
        )
        read_only_fields = fields