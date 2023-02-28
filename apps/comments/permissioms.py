from rest_framework.permissions import BasePermission


class IsCommentOfMembers(BasePermission):
    """
    Custom permission to check if a user is a member of a course.
    """
    def has_object_permission(self, request, view, obj):
        return obj.task.course.members.filter(id=request.user.id).exists()