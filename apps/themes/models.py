from django.db import models
from django.contrib.auth import get_user_model

from apps.courses.models import Course


User = get_user_model()


class Theme(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course,
        on_delete=models.CASCADE,
        related_name='topics',
        verbose_name='course'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_theme',
        verbose_name='owner'
        )
    
    
    class Meta:
        verbose_name = 'theme'
        verbose_name_plural = 'themes'
        
    def __str__(self):
        return f'{self.id}---{self.course}'
