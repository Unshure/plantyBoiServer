from rest_framework import viewsets
from .serializers import SensorDataSerializer
from .models import SensorData
from rest_framework.response import Response

import logging
logger = logging.getLogger(__name__)


class SensorDataView(viewsets.ModelViewSet):
    """
    API endpoint that allows Sensor Data to be viewed or edited
    """
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer