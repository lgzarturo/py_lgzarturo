from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from articles.models import Article, Category
from profiles.models import SocialNetwork


def index(request):
    article_list = Article.objects.filter(is_draft=False)
    paginator = Paginator(article_list, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    categories = Category.objects.all()
    social_networks = SocialNetwork.objects.all()
    context = {
        'articles': articles,
        'categories': categories,
        'social_networks': social_networks,
    }
    return render(request, 'articles/index.html', context)


def category_article(request, slug):
    article_list = Article.objects.filter(is_draft=False, category__slug=slug)
    paginator = Paginator(article_list, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    categories = Category.objects.all()
    social_networks = SocialNetwork.objects.all()
    context = {
        'articles': articles,
        'categories': categories,
        'social_networks': social_networks,
    }
    return render(request, 'articles/index.html', context)


def show(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'article': article
    }
    return render(request, 'articles/show.html', context)
