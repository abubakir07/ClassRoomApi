from rest_framework.permissions import BasePermission


class IsUserOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.id == obj.id)


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.id == obj.owner.id)


class IsTeacher(BasePermission):
    """
    Пользователь является учителем курса или только чтение.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешено редактирование только учителю курса
        return bool(obj.teacher.id == request.user.id)


class IsMemberOfCourse(BasePermission):
    """
    Custom permission to check if a user is a member of a course.
    """
    def has_object_permission(self, request, view, obj):
        return obj.members.filter(id=request.user.id).exists()
    