from rest_framework.permissions import BasePermission 


class IsTeacherForFeedbacks(BasePermission):
    """
    Пользователь является учителем курса или только чтение.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешено редактирование только учителю курса
        return bool(obj.task.task.course.teacher == request.user)