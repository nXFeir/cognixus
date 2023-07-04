from rest_framework import serializers

from .models import TodoItem

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['uuid', 'user', 'title', 'start_time', 'is_completed', 'created_at']
        extra_kwargs = {
            'user': {'write_only': True},
        }

            