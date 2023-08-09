from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer

# HTML Rendering View
def asset_list(request):
    companies = Company.objects.all()
    employees = Employee.objects.all()
    devices = Device.objects.all()
    device_logs = DeviceLog.objects.all()

    context = {
        'companies': companies,
        'employees': employees,
        'devices': devices,
        'device_logs': device_logs,
    }
    
    return render(request, 'index.html', context)


# API Viewsets
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

# with the above configuration, you can use the following endpoints for CRUD operations:

# List: GET /api/companies/
# Create: POST /api/companies/
# Retrieve: GET /api/companies/{id}/
# Update: PUT /api/companies/{id}/
# Partial Update: PATCH /api/companies/{id}/
# Delete: DELETE /api/companies/{id}/
# The same endpoints apply for employees, devices, and device-logs. Replace companies with the respective model name in the URL to access the endpoints for other models.