from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.resume.selectors.resume import my_resume
from apps.analytics.models import AnalyticsEventType
from apps.analytics.tasks import record_analytics_event

from apps.pdf.services import (
    enqueue_resume_pdf,
    pdf_status,
)

from apps.pdf.selectors import (resume_pdf_path)


class ResumePDFGenerateAPIView(APIView):
    permission_classes = (IsAuthenticated)

    def post(self, request):
        resume = my_resume(request.user)
        enqueue_resume_pdf(resume=resume)

        return Response(
            {
                "detail": "PDF generation started.",
            }
        )


class ResumePDFStatusAPIView(APIView):
    permission_classes = (IsAuthenticated)

    def get(self, request):
        return Response(
            pdf_status(
                resume=my_resume(
                    request.user,
                )
            )
        )


class ResumePDFDownloadAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        resume = my_resume(request.user)
        
        record_analytics_event.delay(
            resume.id,
            AnalyticsEventType.PDF_DOWNLOAD,
            request.META.get("REMOTE_ADDR"),
            request.META.get("HTTP_USER_AGENT", ""),
        )
        return FileResponse(
            open(
                resume_pdf_path(resume),
                "rb",
            ),
            content_type="application/pdf",
        )
        