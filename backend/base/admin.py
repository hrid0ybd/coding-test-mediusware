from django.contrib import admin
from .models import Persons


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'village', 'district', 'division')
    list_filter = ('date_created', 'division')
    search_fields = ['dna_sample_id', 'nid_bid']


# Register your models here.
admin.site.site_header = 'Coding Test - Mediusware Ltd.'
admin.site.register(Persons, PersonAdmin)
