from rest_framework.permissions import BasePermission


class UserViewPermissions(BasePermission):
    """
    User permissions.
    """

    def has_permission(self, request, view):
        if view.action in ['list', 'create', 'retrieve']:
            # Allow anyone to create an account
            return True

        if view.action in ['destroy']:
            # Only authorized users can delete their account
            return not request.user.is_anonymous

        return False
