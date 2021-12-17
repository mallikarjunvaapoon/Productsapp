from rest_framework import serializers
from .models import Connection_request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection_request
        fields = ['status_of', 'sender', 'receiver']




