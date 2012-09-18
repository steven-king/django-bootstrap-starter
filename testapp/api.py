from djangorestframework.resources import ModelResource
from testapp.models import Person


class PersonResource(ModelResource):
    model = Person
    