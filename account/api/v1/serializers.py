from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from ...models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    country = CountryField()

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
    country = CountryField()

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
