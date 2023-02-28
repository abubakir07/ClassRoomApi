from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.comments.models import Comment
from apps.comments.permissioms import IsCommentOfMembers
from apps.comments.serializers import CommentSerializer
from utils.permissions import IsOwner


class CommentApiViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwner()]
        return [IsCommentOfMembers()]
