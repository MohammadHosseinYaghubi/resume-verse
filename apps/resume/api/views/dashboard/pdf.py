from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.resume.selectors.resume import (
    my_resume,
)

from apps.pdf.services import (
    enqueue_resume_pdf,
    pdf_status,
)


class DashboardPDFAPIView(APIView):

    permission_classes = (
        IsAuthenticated,
    )

    def get(
        self,
        request,
    ):

        resume = my_resume(
            request.user,
        )

        return Response(

            pdf_status(
                resume=resume,
            )

        )

    def post(
        self,
        request,
    ):

        resume = my_resume(
            request.user,
        )

        enqueue_resume_pdf(
            resume=resume,
        )

        return Response(

            {

                "status": "processing",

            },

            status=202,

        )