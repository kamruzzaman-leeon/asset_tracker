from django.test import TestCase
from django.urls import reverse
from .models import Company, Employee, Device, DeviceLog
from datetime import datetime, timedelta

class CompanyModelTest(TestCase):
    def test_company_str_method(self):
        company = Company.objects.create(name="Test Company")
        self.assertEqual(str(company), "Test Company")

class CompanyViewTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Test Company")
        self.url = reverse("company-detail", args=[self.company.id])

    def test_company_list_view(self):
        response = self.client.get(reverse("company-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.company.name)

    def test_company_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.company.name)        

class EmployeeModelTest(TestCase):
    def test_employee_str_method(self):
        company = Company.objects.create(name="Test Company")
        employee = Employee.objects.create(name="fahim", company=company)
        self.assertEqual(str(employee), "fahim")

class EmployeeViewTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Test Company")
        self.employee = Employee.objects.create(name="shawon ahmed", company=self.company)
        self.url = reverse("employee-detail", args=[self.employee.id])

    def test_employee_list_view(self):
        response = self.client.get(reverse("employee-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.employee.name)

    def test_employee_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.employee.name)

class DeviceLogModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Test Company")
        self.employee = Employee.objects.create(name="shawon ahmed", company=self.company)
        self.device = Device.objects.create(name="Test Device", condition="Good")

    def test_devicelog_str_method(self):
        today = datetime.now()
        log = DeviceLog.objects.create(
            device=self.device,
            employee=self.employee,
            checked_out_date=today,
            condition_when_checked_out="Good",
            returned_date=today + timedelta(days=5),
            condition_when_returned="Fair"
        )
        expected_str = f"{self.device} - {self.employee} - Checkout: {today}, Return: {today + timedelta(days=5)}"
        self.assertEqual(str(log), expected_str)

# class DeviceLogViewTest(TestCase):
#     def setUp(self):
#         self.company = Company.objects.create(name="Test Company")
#         self.employee = Employee.objects.create(name="fahim rahman", company=self.company)
#         self.device = Device.objects.create(name="Test Device", condition="Good")
#         self.log = DeviceLog.objects.create(
#             device=self.device,
#             employee=self.employee,
#             checked_out_date=datetime.now(),
#             condition_when_checked_out="Good",
#             returned_date=datetime.now() + timedelta(days=5),
#             condition_when_returned="Fair"
#         )
#         self.url = reverse("devicelog-detail", args=[self.log.id])  

#     def test_devicelog_list_view(self):
#         response = self.client.get(reverse("devicelog-list"))  
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, self.log.device.name)
#         self.assertContains(response, self.log.employee.name)

#     def test_devicelog_detail_view(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, self.log.device.name)
#         self.assertContains(response, self.log.employee.name)






#to run test 
