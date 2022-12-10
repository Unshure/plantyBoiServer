from django.contrib import admin
from .models import SensorData

class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'data', 'createdAt')

# Register your models here.

admin.site.register(SensorData, SensorDataAdmin)