from rest_framework.exceptions import APIException


class PDFGenerationError(APIException):

    status_code = 500

    default_detail = "Unable to generate PDF."