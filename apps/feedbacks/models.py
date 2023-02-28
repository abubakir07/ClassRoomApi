from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.tasks.models import TaskSubmission


User = get_user_model()


class Feedback(models.Model):
    task = models.ForeignKey(
        TaskSubmission,
        on_delete=models.CASCADE,
        related_name='feedback',
        verbose_name='task submission'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='feedback_owner',
        verbose_name='owner'
    )
    score = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='score'
    )
    comment = models.CharField(
        max_length=255,
        verbose_name='comment',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created at'
    )
    
    