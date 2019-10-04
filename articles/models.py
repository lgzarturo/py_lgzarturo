from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from profiles.models import Profile


class Category(models.Model):
    slug = models.SlugField(unique=True, verbose_name=_('Identificador'))
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Nombre de la categoría'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Categoría')
        verbose_name_plural = _('Categorías')


class Article(models.Model):
    slug = models.SlugField(unique=True, verbose_name=_('Identificador'))
    title = models.CharField(max_length=255, unique=True, verbose_name=_('Título'))
    excerpt = models.CharField(max_length=140, blank=True, verbose_name=_('Resumen'))
    content = models.TextField(verbose_name=_('Contenido'))
    is_draft = models.BooleanField(default=True, verbose_name=_('¿Borrador?'))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name=_('Categoría'))
    thumbnail = models.ImageField(upload_to='thumbs', null=True, blank=True, verbose_name=_('Portada'))
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_('Autor'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def time_read(self):
        return "%s" % (len(self.content.split()) / 200)

    def get_absolute_url(self):
        return reverse("blog_show", args=[self.slug])

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = _('Artículo')
        verbose_name_plural = _('Artículos')
