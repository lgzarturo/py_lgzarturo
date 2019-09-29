from django.shortcuts import render

from articles.models import Article
from projects.models import Project


def index(request):
    articles = Article.objects.all()
    projects = Project.objects.all()
    context = {
        'articles': articles,
        'projects': projects,
    }
    return render(request, 'web/index.html', context)
