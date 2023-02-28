from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime

from .models import Task


@shared_task
def send_task_email(task_id):
    task = Task.objects.get(id=task_id)
    subject = f"New Task: {task.title}"
    message = f"Dear {task.course.members},\n\nA new task has been added to the {task.course.name} course: {task.title}.\n\nTask description: {task.description}\n\nDeadline: {task.deadline}\n\nBest regards,\nThe Course Management Team"
    from_email = "course_management@example.com"
    recipient_list = [member.email for member in task.course.members.all()]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    
    if task.deadline and datetime.now() > task.deadline:
        subject = f"Overdue Task: {task.title}"
        message = f"Dear {task.owner.username},\n\nYou have an overdue task for the {task.course.name} course: {task.title}.\n\nDeadline: {task.deadline}\n\nBest regards,\nThe Course Management Team"
        recipient_list = [task.owner.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
