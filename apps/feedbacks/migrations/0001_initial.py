# Generated by Django 4.1.7 on 2023-02-28 16:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0005_remove_tasksubmission_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='score')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_owner', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='tasks.tasksubmission')),
            ],
        ),
    ]
