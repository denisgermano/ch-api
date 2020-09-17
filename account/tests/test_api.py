import random

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Company
from .factory import CompanyFactory, EmployeeFactory


class AccountV1TestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.empty_company = CompanyFactory()
        cls.nice_company = CompanyFactory()
        cls.employee = EmployeeFactory(companies=[cls.nice_company])


class AccountCompanyV1TestCase(AccountV1TestCase):
    def test_fail_create_missing_all_required_fields(self):
        url = reverse("company-list")
        data = {}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertListEqual(
            [
                "name",
                "document",
                "address",
                "country",
            ],
            list(response.data.keys()),
        )

    def test_fail_create_wrong_country(self):
        url = reverse("company-list")
        data = {
            "name": "My company",
            "document": "12.123.123.1234-12",
            "address": "My street, 10",
            "country": "asdf",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("country", response.data.keys())

    def test_success_create(self):
        url = reverse("company-list")
        data = {
            "name": "My company",
            "document": "12.123.123.1234-12",
            "address": "My street, 10",
            "country": "BR",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_companies(self):
        url = reverse("company-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Company.objects.count())

    def test_detail_company(self):
        url = reverse("company-detail", args=[self.empty_company.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), self.empty_company.id)
        self.assertEqual(response.data.get("name"), self.empty_company.name)

    def test_detail_company_without_employees(self):
        url = reverse("company-detail", args=[self.empty_company.id])
        response = self.client.get(f"{url}employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(response.data, [])

    def test_detail_company_with_employees(self):
        url = reverse("company-detail", args=[self.nice_company.id])
        response = self.client.get(f"{url}employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get("username"), self.employee.username)

    def test_success_delete(self):
        url = reverse("company-detail", args=[self.empty_company.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_fail_delete(self):
        url = reverse("company-detail", args=[0])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AccountEmployeeV1TestCase(AccountV1TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee_no_company = EmployeeFactory()
        cls.other_company = CompanyFactory()
        cls.employee_mult_company = EmployeeFactory(
            companies=[cls.nice_company, cls.other_company]
        )

    def test_fail_create_missing_all_required_fields(self):
        url = reverse("employee-list")
        data = {}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertListEqual(
            [
                "username",
                "document",
                "address",
                "country",
            ],
            list(response.data.keys()),
        )

    def test_fail_create_repeated_username(self):
        url = reverse("employee-list")
        data = {
            "username": self.employee.username,
            "document": "12.123.123.1234-12",
            "address": "My street, 10",
            "country": "BR",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data.keys())

    def test_success_create(self):
        url = reverse("employee-list")
        username = str(random.randint(0, 10))
        data = {
            "username": username,
            "document": "12.123.123.1234-12",
            "address": "My street, 10",
            "country": "BR",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_employee(self):
        url = reverse("employee-detail", args=[self.employee.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), self.employee.id)
        self.assertEqual(response.data.get("companies"), [self.nice_company.id])

    def test_detail_employee_no_company(self):
        url = reverse("employee-detail", args=[self.employee_no_company.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), self.employee_no_company.id)
        self.assertEqual(response.data.get("companies"), [])

    def test_detail_employee_mult_company(self):
        url = reverse("employee-detail", args=[self.employee_mult_company.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), self.employee_mult_company.id)
        self.assertEqual(
            response.data.get("companies"),
            [self.nice_company.id, self.other_company.id],
        )
