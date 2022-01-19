
from django.shortcuts import render, get_object_or_404
from .models import Article, Team

# Create your views here.

def index(request):
    return render(request, 'index.html')

def articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles.html', context)

def about(request):
    all_team = Team.objects.all()
    context = {
        'all_team': all_team
    }
    return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html')

def detail(request, article_id):
    single_article = get_object_or_404(Article, pk=article_id)
    context = {
        'single_article': single_article,
    }
    return render(request, 'article-details.html', context)
