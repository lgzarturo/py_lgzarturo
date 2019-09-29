from django.contrib import admin

from catalogs.models import Company, School, SkillType
from .models import Network


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(SkillType)
class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']
