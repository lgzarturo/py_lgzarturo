from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from profiles.models import Profile, Work, Education, Skill, SocialNetwork


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    summernote_fields = ('about_me', )
    list_display = ('slug', 'first_name', 'last_name', )
    prepopulated_fields = {"slug": ("first_name", "last_name", )}
    ordering = ['created']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'title', 'profession', 'about_me', 'location']


@admin.register(Work)
class WorkAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('company', )
    ordering = ['created']
    search_fields = ['company__name', 'position', 'location']
    autocomplete_fields = ['company']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', )
    ordering = ['created']
    search_fields = ['school__name', 'certification']
    autocomplete_fields = ['school']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ['created']
    search_fields = ['name', 'type__name']
    autocomplete_fields = ['type']


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ['created']
    search_fields = ['name', 'network__name']
    autocomplete_fields = ['network']
