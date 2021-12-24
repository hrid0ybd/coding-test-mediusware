from rest_framework import viewsets
from . import models
from . import serializers


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Persons.objects.all()
    serializer_class = serializers.PersonSerializer
