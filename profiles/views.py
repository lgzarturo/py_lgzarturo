from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import View

from profiles.models import SocialNetwork
from profiles.render import Render
from .models import Profile, Work, Education, Skill


def index(request):
    profile = get_object_or_404(Profile, pk=1)
    works = Work.objects.filter(profile=profile).order_by('created', 'is_actual')
    educations = Education.objects.filter(profile=profile).order_by('created')
    skills = Skill.objects.filter(profile=profile).order_by('created')
    social_networks = SocialNetwork.objects.filter(profile=profile).order_by('created')
    context = {
        'profile': profile,
        'works': works,
        'educations': educations,
        'skills': skills,
        'social_networks': social_networks,
    }
    return render(request, 'profiles/index.html', context)


class Pdf(View):

    def get(self, request):
        profile = get_object_or_404(Profile, pk=1)
        works = Work.objects.filter(profile=profile).order_by('created', 'is_actual')
        educations = Education.objects.filter(profile=profile).order_by('created')
        skills = Skill.objects.filter(profile=profile).order_by('created')
        social_networks = SocialNetwork.objects.filter(profile=profile).order_by('created')
        today = timezone.now()
        photo_url = request.build_absolute_uri(profile.photo.url)
        params = {
            'today': today,
            'profile': profile,
            'works': works,
            'educations': educations,
            'skills': skills,
            'social_networks': social_networks,
            'request': request,
            'photo_url': photo_url,
        }
        return Render.render('profiles/pdf.html', params)
