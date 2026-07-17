from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from apps.common.api.viewsets import BaseViewSet
from apps.resume.selectors.resume import my_resume
from apps.analytics.selectors import get_resume_analytics
from .serializers import ResumeAnalyticsSerializer


class DashboardAnalyticsViewSet(mixins.RetrieveModelMixin, BaseViewSet):

    permission_classes = (IsAuthenticated)
    serializer_class = ResumeAnalyticsSerializer
    lookup_field = "id"

    def get_object(self):
        resume = my_resume(self.request.user)
        return get_resume_analytics(resume=resume)