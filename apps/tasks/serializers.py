from rest_framework import serializers

from apps.tasks.models import Task, TaskSubmission
        

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = ('owner',)
        fields = (
            'id',
            'owner',
            'course',
            'title',
            'description',
            'link',
            'file',
            'max_score',
            'deadline',
            'theme',
            )


class TaskSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSubmission
        fields = (
            'id',
            'task',
            'owner',
            'course',
            'text',
            'submission_date',
            'file',
            'link'
            )
        read_only_fields = (
            'submission_date',
            'owner'
            )