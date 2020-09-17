from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django_countries.fields import CountryField

from utils.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=60)
    document = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    country = CountryField()

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}"


class Employee(AbstractUser):
    companies = models.ManyToManyField(Company, related_name="employees", blank=True)
    document = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    salary = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=Decimal(0),
        validators=[MinValueValidator(Decimal(0))],
    )
    country = CountryField()

    def __str__(self):
        return f"{self.username}: {self.get_full_name()}"
