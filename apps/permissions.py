from rest_framework.permissions import BasePermission, BasePermissionMetaclass, IsAuthenticated, SAFE_METHODS
class CustomAdminPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        print(user)
        return bool(request.user.is_authenticated and user.is_superuser)

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS