from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from catalogs.models import Network, SkillType, School, Company


class Profile(models.Model):
    slug = models.SlugField(db_index=True, verbose_name=_('Identificador'))
    first_name = models.CharField(max_length=255, db_index=True, verbose_name=_('Nombre'))
    last_name = models.CharField(max_length=255, db_index=True, verbose_name=_('Apellidos'))
    photo = models.ImageField(upload_to="photos", verbose_name=_('Foto'))
    title = models.CharField(max_length=255, verbose_name=_('Título'))
    profession = models.CharField(max_length=255, verbose_name=_('Profesión'))
    about_me = models.TextField(verbose_name=_('Sobre mí'))
    location = models.CharField(max_length=64, verbose_name=_('Ubicación'))
    postal_code = models.CharField(max_length=10, verbose_name=_('Código postal'))
    summary = models.CharField(max_length=255, verbose_name=_('Resumen'))
    phone = models.CharField(max_length=32, db_index=True, verbose_name=_('Teléfono'))
    email = models.EmailField(db_index=True, verbose_name=_('Correo electrónico'))
    website = models.URLField(db_index=True, verbose_name=_('Sitio web'))
    birth_date = models.DateField(verbose_name=_('Fecha de nacimiento'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Usuario'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _('Perfil')
        verbose_name_plural = _('Perfiles')


class Work(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name=_('Compañía'))
    position = models.CharField(max_length=255, verbose_name=_('Posición'))
    location = models.CharField(max_length=255, verbose_name=_('Ubicación'))
    description = models.TextField(verbose_name=_('Descripción'))
    start_date = models.DateField(verbose_name=_('Fecha de inicio'))
    end_date = models.DateField(null=True, blank=True, verbose_name=_('Fecha de renuncia'))
    is_actual = models.BooleanField(default=False, verbose_name=_('Trabajo actual'))
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_('Perfil'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def __str__(self):
        return "%s" % self.company

    class Meta:
        verbose_name = _('Empleo')
        verbose_name_plural = _('Empleos')


class Education(models.Model):
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, verbose_name=_('Institución'))
    certification = models.CharField(max_length=64, verbose_name=_('Título o certificado'))
    start_year = models.PositiveSmallIntegerField(default=0, verbose_name=_('Año de inicio'))
    end_year = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name=_('Año de egreso'))
    is_actual = models.BooleanField(default=False, verbose_name=_('Cursando'))
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_('Perfil'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def __str__(self):
        return "%s" % self.school

    class Meta:
        verbose_name = _('Escolaridad')
        verbose_name_plural = _('Escolaridades')


class Skill(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('Habilidad'))
    percentage = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name=_('Porcentaje de experiencia'))
    years = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name=_('Años de experiencia'))
    type = models.ForeignKey(SkillType, on_delete=models.SET_NULL, null=True, verbose_name=_('Tipo de habilidad'))
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_('Perfil'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Habilidad')
        verbose_name_plural = _('Habilidades')


class SocialNetwork(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('Nombre'))
    network = models.ForeignKey(Network, on_delete=models.SET_NULL, null=True, verbose_name=_('Red social'))
    url = models.URLField(verbose_name=_('Enlace'))
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_('Perfil'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Última actualización'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Red social')
        verbose_name_plural = _('Redes sociales')


class ProfileView(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_('Perfil'))
    views = models.PositiveIntegerField(default=0, verbose_name=_('Visitas'))
    searches = models.PositiveIntegerField(default=0, verbose_name=_('Búsquedas'))
    publication_views = models.PositiveIntegerField(default=0, verbose_name=_('Visitas en publicaciones'))

    def __str__(self):
        return "%s" % self.profile.__str__()

    class Meta:
        verbose_name = _('Visita')
        verbose_name_plural = _('Visitas')
