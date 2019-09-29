from django.db import models
from django.utils.translation import ugettext_lazy as _


class Lead(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Nombre del prospecto'))
    email = models.EmailField(verbose_name=_('Correo electrónico'))
    website = models.URLField(blank=True, verbose_name=_('Sitio web'))
    phone = models.CharField(max_length=255, blank=True, verbose_name=_('Teléfono'))
    message = models.TextField(verbose_name=_('Mensaje'))
    source = models.CharField(max_length=255, verbose_name=_('Fuente'))
    medium = models.CharField(max_length=255, verbose_name=_('Medio'))
    campaign = models.CharField(max_length=255, verbose_name=_('Campaña'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Prospecto')
        verbose_name_plural = _('Prospectos')
