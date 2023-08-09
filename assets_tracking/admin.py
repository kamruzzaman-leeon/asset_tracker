from django.contrib import admin
from .models import Company, Employee, Device, DeviceLog

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(DeviceLog)

#Registered the model to admin.py to access the django admin interface by visting the url 'http://127.0.0.1:8000/admin/'