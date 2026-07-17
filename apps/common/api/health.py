from django.db import connections
from django.db.utils import OperationalError

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from apps.common.api.responses import success_response


class HealthCheckAPIView(APIView):

    permission_classes = (
        AllowAny,
    )

    authentication_classes = ()

    def get(
        self,
        request,
    ):

        database = "ok"

        try:

            connections["default"].cursor()

        except OperationalError:

            database = "error"

        return success_response(
            data={
                "status": "ok" if database == "ok" else "error",
                "database": database,
            },
        )