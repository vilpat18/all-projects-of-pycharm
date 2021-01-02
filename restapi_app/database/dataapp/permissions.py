from rest_framework.permissions import BasePermission ,SAFE_METHODS

class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class AllPermission(BasePermission):
    def has_permission(self, request, view):
        allowed_methods = ['GET','POST', 'PUT', 'PATCH', 'DELETE']
        if request.method in allowed_methods:
            return True
        else:
            return False