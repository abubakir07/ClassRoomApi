from django.db.models import Q
from rest_framework import viewsets, permissions

from apps.feedbacks.permissions import IsTeacherForFeedbacks
from utils.permissions import IsOwner
from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Feedback.objects.filter(task__owner=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'list', 'update', 'partial_update']:
            return (IsTeacherForFeedbacks(),)
        elif self.action == 'retrieve':
            return (IsOwner(),)
        return []
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
