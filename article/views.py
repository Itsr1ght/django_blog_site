from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def article_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, "article_list.html", { 'articles': articles})

def article_page(request , slug):
    article = Article.objects.get(slug=slug)
    return render(request, "article_page.html", {'article':article})