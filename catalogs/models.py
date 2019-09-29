from django.db import models
from django.utils.translation import ugettext_lazy as _


class Network(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('Nombre de la red'))
    icon = models.CharField(max_length=32, verbose_name=_('Icono'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Red')
        verbose_name_plural = _('Redes')


class Company(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('Nombre de la compañía'))
    description = models.TextField(verbose_name=_('Descripción'))
    location = models.CharField(max_length=64, verbose_name=_('Ubicación'))
    website = models.URLField(verbose_name=_('Sitio web'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Compañía')
        verbose_name_plural = _('Compañías')


class School(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('Institución'))
    description = models.TextField(verbose_name=_('Descripción'))
    location = models.CharField(max_length=64, verbose_name=_('Ubicación'))
    website = models.URLField(verbose_name=_('Sitio web'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Institución')
        verbose_name_plural = _('Instituciones')


class SkillType(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('Nombre de la habilidad'))
    description = models.TextField(verbose_name=_('Descripción'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Tipo de habilidad')
        verbose_name_plural = _('Tipos de habilidad')
