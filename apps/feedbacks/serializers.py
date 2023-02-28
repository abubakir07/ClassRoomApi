from rest_framework import serializers

from apps.feedbacks.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'id',
            'task',
            'owner',
            'score',
            'comment'
        )
        read_only_fields = (
            'owner',
            'create_at'
            )
        