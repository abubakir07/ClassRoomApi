from django.contrib.auth import get_user_model
from django.db import models

# from apps.tasks.models import Task


User = get_user_model()


class Course(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=50)
    image = models.ImageField(
        upload_to='post_images/',
        verbose_name='image',
        null=True,
        blank=True
        )
    chapter = models.CharField(
        max_length=50,
        verbose_name='chapter',
        null=True,
        blank=True
        )
    item = models.CharField(
        max_length=50,
        verbose_name='item',
        null=True,
        blank=True
        )
    audience = models.CharField(
        max_length=50,
        verbose_name='audience',
        null=True,
        blank=True
        )
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='teacher',
        verbose_name='teacher',
    )
    members = models.ManyToManyField(
        User,
        related_name='members',
        verbose_name='members',
        null=True,
        blank=True
    )   

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'Courses'
    
    def __str__(self):
        return f'{self.name}'
    




