from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser or request.user.is_staff:
            return True

        user = obj.user

        # Write permissions are only allowed to the owner of the snippet.
        return user.username == request.user.username

class IsAgenciadoOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser or request.user.is_staff:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user.id == request.user.id
