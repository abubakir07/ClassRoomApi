from django.contrib import admin

from apps.tasks.models import Task, TaskSubmission

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']

@admin.register(TaskSubmission)
class TaskSubmissionAdmin(admin.ModelAdmin):
    list_display = ['id','task', 'owner', 'course']
    list_editable = ['task']