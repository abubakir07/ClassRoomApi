# Generated by Django 4.1.7 on 2023-02-28 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0002_theme_owner'),
        ('tasks', '0005_remove_tasksubmission_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='theme', to='themes.theme', verbose_name='theme'),
        ),
    ]