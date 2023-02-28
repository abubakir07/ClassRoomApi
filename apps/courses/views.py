from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from apps.courses.models import Course
from apps.courses.serializers import CourseSerializer
from utils.permissions import IsTeacher, IsMemberOfCourse


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)
    
    def get_permissions(self):
        if self.action in ["partial_update", "update", "destroy"]:
            return [IsTeacher(), IsAuthenticated()]
        elif self.action in ["list","retrieve",]:
            return [IsMemberOfCourse()]
        return [IsAuthenticated()]
   
    def get_queryset(self): 
        return Course.objects.filter(Q(members=self.request.user) | Q(teacher=self.request.user)).distinct()

   