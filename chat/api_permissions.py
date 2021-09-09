from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # TODO убрать потом пермишн на Анонима
        elif obj.username == 'Anonymous':
            return True
        return obj.username == request.user.username
