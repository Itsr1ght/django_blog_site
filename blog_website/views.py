from django.http import HttpResponse
from django.shortcuts import render
from article.models import Article

def home_page(request):
    article = Article.objects.all().order_by('-date')[0]
    return render(request,'home.html',{ "article" : article })


def about_page(request):
    return render(request,'about.html')