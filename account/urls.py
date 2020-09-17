from django.urls import include, path
from rest_framework import routers

from account.views.v1 import CompanyViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r"employees", EmployeeViewSet)
router.register(r"companies", CompanyViewSet)

urlpatterns = [
    path("v1/employees/<str:username>/", EmployeeViewSet.as_view({"get": "retrieve"})),
    path("v1/", include(router.urls)),
]
