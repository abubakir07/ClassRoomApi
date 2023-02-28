from django.db import models
from django.contrib.auth import get_user_model

from apps.courses.models import Course
from apps.themes.models import Theme


User = get_user_model()


class Task(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='title')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='creator',
        verbose_name='owner'
        )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name='course',
        verbose_name='course')
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE,
        related_name='theme',
        verbose_name='theme',
        null=True,
        blank=True
        )
    description = models.TextField(
        verbose_name='description',
        null=True,
        blank=True
        )
    file = models.FileField(
        verbose_name='file',
        upload_to='task_files/',
        blank=True
        )
    link = models.URLField(
        verbose_name='link',
        null=True,
        blank=True
        )
    max_score = models.PositiveIntegerField(
        verbose_name='max score',
        default=100
        )
    deadline = models.DateTimeField(
        verbose_name='deadline',
        blank=True,
        null=True
        )

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self):
        return f'{self.title}---{self.course.name}'


class TaskSubmission(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='task_submission'
        )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_submission',
        verbose_name='owner submission'
        )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='course_task', 
        verbose_name='course'
        )
    text = models.CharField(
        max_length=255
    )
    submission_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(
        verbose_name='file',
        upload_to='submitted_tasks/',
        null=True,
        blank=True)
    link = models.URLField(
        null=True,
        blank=True
        )

    class Meta:
        verbose_name = 'task submission'
        verbose_name_plural = 'Task submission'
    
    def __str__(self):
        return f'{self.task.title} ({self.owner.username})'
