from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Project


@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', )
    prepopulated_fields = {"slug": ("title",)}
