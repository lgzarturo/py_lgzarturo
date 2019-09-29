from django.db import models
from django.utils.translation import ugettext_lazy as _

from profiles.models import Profile


class Project(models.Model):
    slug = models.SlugField(unique=True, verbose_name=_('Identificador'))
    title = models.CharField(max_length=255, unique=True, verbose_name=_('Título'))
    excerpt = models.CharField(max_length=140, null=True, blank=True, verbose_name=_('Resumen'))
    thumbnail = models.ImageField(upload_to='thumbs', null=True, blank=True, verbose_name=_('Portada'),
                                  help_text=_('La imagen debe tener una proporción 1:1, de preferencia 500x500'))
    content = models.TextField(verbose_name=_('Descripción'))
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_('Autor'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def time_read(self):
        return round(len(self.content.split()) / 200, 2)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = _('Proyecto')
        verbose_name_plural = _('Proyectos')
