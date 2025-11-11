from django.contrib import admin
from django.urls import path,include
from django_distill import distill_path
from .models import Article

from . import views

import os


def get_none():
    return None

def get_article_slugs():
    for article in Article.objects.all():
        yield (article.slug,)



if os.getenv("GITHUB_ACTIONS"):
    urlpatterns = [
        distill_path(
            '',views.article_list, name="article_list",
            distill_func=get_none, distill_file='article/index.html',
        ),
        distill_path(
            '<slug>',views.article_page, name="article_page",
            distill_func=get_article_slugs, distill_file='article/{0}/index.html'
        )
    ]
else:
    urlpatterns = [
        path('',views.article_list, name="article_list"),
        path('<slug>',views.article_page, name="article_page")
    ]
