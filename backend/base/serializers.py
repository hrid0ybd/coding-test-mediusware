from django.db.models import fields
from rest_framework import serializers
from base.models import Persons


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ('personId', 'name', 'image', 'division', 'district', 'upozila', 'village', 'address', 'date_of_birth', 'marital_status',
                  'nid_bid', 'dna_sample_id', 'date_created', 'is_late')
