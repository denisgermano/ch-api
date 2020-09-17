from django.contrib import admin

from account.models import Company, Employee


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("username", "name", "current_companies")
    filter_horizontal = ('companies',)

    def name(self, obj):
        return obj.get_full_name()

    name.short_description = "Name"

    def current_companies(self, obj):
        companies = ""
        for i, company in enumerate(obj.companies.all().values_list("name", flat=True)):
            if i == 0:
                companies += f"{company}"
                continue
            companies += f", {company}"
        return companies

    current_companies.short_description = "Companies"
