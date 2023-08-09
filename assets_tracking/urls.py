from django.urls import path, include
from rest_framework import routers
from . import views
#Import necessary modules and classes: path for defining URL patterns, include for including other URL configurations, routes, and the views for your API views.

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'devices',views.DeviceViewSet)
router.register(r'device-logs', views.DeviceLogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.asset_list, name='asset_list'),
]
