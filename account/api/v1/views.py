from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ...models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.prefetch_related("employees").all()

    @action(detail=True, methods=("get",))
    def employees(self, request, pk=None):
        company = self.get_object()
        serializer = EmployeeSerializer(company.employees.all(), many=True)
        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = "username"
