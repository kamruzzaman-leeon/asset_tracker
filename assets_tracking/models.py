# assets_tracking/models.py

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=100)    
    condition = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.condition}"

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_date = models.DateTimeField()
    condition_when_checked_out = models.CharField(max_length=100)
    returned_date = models.DateTimeField(blank=True,null=True)    
    condition_when_returned = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.device} - {self.employee} - Checkout: {self.checked_out_date}, Return: {self.returned_date}"
