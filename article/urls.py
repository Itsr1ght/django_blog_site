from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.article_list),
    path('<slug>',views.article_page)
]
