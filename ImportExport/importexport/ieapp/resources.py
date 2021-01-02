from import_export import resources

from .models import Employee,Person

class PersonResources(resources.ModelResource):
    class Meta:
        model = Person


class EmployeeResources(resources.ModelResource):
    class Meta:
        model = Employee