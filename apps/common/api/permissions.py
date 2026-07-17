from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):

    """
    Read for everyone.

    Write only for admins.
    """

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:

            return True

        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )
    
class IsOwner(BasePermission):

    def has_object_permission(
        self,
        request,
        view,
        obj,
    ):

        return obj.user == request.user