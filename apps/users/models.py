from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(
        upload_to='user_images/',
        verbose_name='image',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "user"
        verbose_name_plural = 'Users'

    def __str__(self):
       return f'Username: {self.username}'
