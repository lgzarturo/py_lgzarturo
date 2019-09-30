from django.shortcuts import render

from articles.models import Article
from projects.models import Project


def index(request):
    articles = Article.objects.filter(is_draft=False)[:6]
    projects = Project.objects.all()[:6]
    context = {
        'articles': articles,
        'projects': projects,
    }
    return render(request, 'web/index.html', context)
