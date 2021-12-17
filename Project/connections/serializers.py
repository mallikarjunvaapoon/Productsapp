from rest_framework import serializers
from .models import Connection_request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection_request
        fields = ['requested', 'sender', 'receiver']




