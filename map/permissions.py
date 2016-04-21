from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    Is it the correct user based on username
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsProfileOwner(permissions.BasePermission):
    """
    Only allow profile owner to view and edit.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
