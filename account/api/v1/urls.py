from django.urls import include, path
from rest_framework import routers

from .views import CompanyViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r"employees", EmployeeViewSet)
router.register(r"companies", CompanyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
