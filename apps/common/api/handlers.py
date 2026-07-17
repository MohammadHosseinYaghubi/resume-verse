from rest_framework.views import (
    exception_handler,
)

from apps.common.api.responses import (
    error_response,
)


def custom_exception_handler(
    exc,
    context,
):

    response = exception_handler(
        exc,
        context,
    )

    if response is None:
        return response

    message = "Request failed."

    if isinstance(
        response.data,
        dict,
    ):

        if "detail" in response.data:
            message = response.data["detail"]

    return error_response(
        errors=response.data,
        message=message,
        status_code=response.status_code,
    )