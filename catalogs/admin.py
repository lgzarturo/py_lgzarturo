from django.contrib import admin

from catalogs.models import Company, School, SkillType
from .models import Network


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', )
    search_fields = ['name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'website', )
    search_fields = ['name']


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'website', )
    search_fields = ['name']


@admin.register(SkillType)
class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    search_fields = ['name']
