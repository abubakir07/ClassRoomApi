from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

# from apps.courses.models import Course
from apps.themes.models import Theme
from apps.themes.serializers import ThemeSerializer
from utils.permissions import IsOwner

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        course = serializer.validated_data['course']
        if course.teacher == self.request.user:
            serializer.save()
        else:
            raise serializers.ValidationError("Only the teacher of the course can create themes")
        
    def get_permissions(self):
        if self.action in ["partial_update", "update", "destroy"]:
            return [IsOwner(),]
        return [IsAuthenticated()] 
