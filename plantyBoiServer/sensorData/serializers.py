from .models import SensorData
from datetime import datetime, timezone
from rest_framework.settings import api_settings
from rest_framework.serializers import ModelSerializer, ValidationError, DateTimeField


import logging

logger = logging.getLogger(__name__)

class SensorDataSerializer(ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('id', 'name', 'data', 'createdAt')