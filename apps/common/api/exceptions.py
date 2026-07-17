from rest_framework import status
from rest_framework.exceptions import APIException


class ResumeAlreadyExists(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Resume already exists."
    default_code = "resume_exists"


class ProjectAlreadyExists(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Project already exists."
    default_code = "project_exists"


class SocialLinkAlreadyExists(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Social link already exists."
    default_code = "social_exists"