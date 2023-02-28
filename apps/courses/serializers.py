from rest_framework import serializers

from apps.tasks.serializers import TaskSerializer
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        read_only_fields = (
            'teacher',
        )
        fields = (
            'id',
            'name',
            'image',
            'chapter',
            'item',
            'audience',
            'teacher',
            'tasks',
            'members'
        )
        
