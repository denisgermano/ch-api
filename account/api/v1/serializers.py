from rest_framework import serializers

from ...models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "document",
            "address",
            "website",
            "country",
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "username",
            "companies",
            "document",
            "address",
            "salary",
            "country",
        ]
