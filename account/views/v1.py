from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Company, Employee
from ..serializers import CompanySerializer, EmployeeSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    @action(detail=True)
    def employees(self, request, *args, **kwargs):
        company = self.get_object()
        serializer = EmployeeSerializer(company.employees.all(), many=True)
        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def retrieve(self, request, username=None, *args, **kwargs):
        obj = get_object_or_404(self.queryset, username=username)
        serializer = EmployeeSerializer(obj)
        return Response(serializer.data)
