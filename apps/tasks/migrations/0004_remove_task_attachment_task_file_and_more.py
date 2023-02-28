# Generated by Django 4.1.7 on 2023-02-28 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0002_theme_owner'),
        ('courses', '0003_alter_course_audience_alter_course_chapter_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_alter_tasksubmission_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='attachment',
        ),
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.FileField(blank=True, upload_to='task_files/', verbose_name='file'),
        ),
        migrations.AddField(
            model_name='tasksubmission',
            name='score',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course', to='courses.course', verbose_name='course'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='deadline'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='link'),
        ),
        migrations.AlterField(
            model_name='task',
            name='max_score',
            field=models.PositiveIntegerField(default=100, verbose_name='max score'),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='task',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme', to='themes.theme', verbose_name='theme'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='tasksubmission',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_task', to='courses.course', verbose_name='course'),
        ),
        migrations.AlterField(
            model_name='tasksubmission',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='submitted_tasks/', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='tasksubmission',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasksubmission',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_submission', to=settings.AUTH_USER_MODEL, verbose_name='owner submission'),
        ),
        migrations.AlterField(
            model_name='tasksubmission',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_submission', to='tasks.task'),
        ),
    ]