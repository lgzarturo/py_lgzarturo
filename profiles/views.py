from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import View

from profiles.models import SocialNetwork
from profiles.render import Render
from .models import Profile, Work, Education, Skill


def index(request):
    profile = get_object_or_404(Profile, pk=1)
    works = Work.objects.filter(profile=profile)
    educations = Education.objects.filter(profile=profile)
    skills = Skill.objects.filter(profile=profile)
    social_networks = SocialNetwork.objects.filter(profile=profile)
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
        works = Work.objects.filter(profile=profile)
        educations = Education.objects.filter(profile=profile)
        skills = Skill.objects.filter(profile=profile)
        social_networks = SocialNetwork.objects.filter(profile=profile)
        today = timezone.now()
        params = {
            'today': today,
            'profile': profile,
            'works': works,
            'educations': educations,
            'skills': skills,
            'social_networks': social_networks,
            'request': request
        }
        return Render.render('profiles/pdf.html', params)
