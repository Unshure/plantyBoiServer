from django.db import models
from datetime import datetime

# Create your models here.

class SensorData(models.Model):
    name = models.CharField(max_length=100)
    data = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return f"Id: {self.pk}, Name: {self.name}, Created At: {self.createdAt}, Data: {self.data}"