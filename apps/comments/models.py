from django.db import models
from django.contrib.auth import get_user_model

from apps.tasks.models import Task


User = get_user_model()


class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        related_name='task_comments',
        verbose_name='task comment',
        on_delete=models.CASCADE
    )
    comment = models.CharField(
        verbose_name='comment',
        max_length=255
    )
    owner = models.ForeignKey(
        User,
        verbose_name='owner',
        related_name='owner_comment',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='parent',
        on_delete=models.SET_NULL,
        related_name='parent_comment',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.owner.username}---{self.task.title}"

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'Comments'
