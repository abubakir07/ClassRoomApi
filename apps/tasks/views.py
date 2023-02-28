from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

from apps.tasks.models import TaskSubmission, Task
from apps.tasks.serializers import TaskSerializer, TaskSubmissionSerializer
from apps.tasks.tasks import send_task_email
from utils.permissions import IsOwner


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_permissions(self):
        if self.action in ["partial_update", "update", "destroy"]:
            return [IsOwner(),]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        task = serializer.save(owner=self.request.user)
        send_task_email.delay(task.id)
        return serializer.save(owner=self.request.user)
    

class TaskSubmissionViewSet(viewsets.ModelViewSet):
    queryset = TaskSubmission.objects.all()
    serializer_class = TaskSubmissionSerializer


    def get_permissions(self):
        if self.action in ["partial_update", "update", "destroy"]:
            return [IsOwner(),]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        course_id = serializer.validated_data['course'].id
        task_course_id = serializer.validated_data['task'].course.id
        if course_id == task_course_id:
            serializer.save(owner=self.request.user)
        else:
            raise serializers.ValidationError("The course of the task does not match the submission course.")
