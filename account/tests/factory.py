import factory
from factory.django import DjangoModelFactory

from account.models import Company, Employee


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker("company")
    document = factory.Faker("ssn")
    address = factory.Faker("street_address")
    website = factory.Faker("hostname")
    country = factory.Faker("country_code")


class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee

    username = factory.Faker("word")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("ascii_email")
    document = factory.Faker("ssn")
    address = factory.Faker("street_address")
    salary = factory.Faker("random_int")
    country = factory.Faker("country_code")

    @factory.post_generation
    def companies(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for company in extracted:
                self.companies.add(company)
