from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from articles.models import Article, Category


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', )
    list_display = ('title', )
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name', ]
    prepopulated_fields = {"slug": ("name",)}
