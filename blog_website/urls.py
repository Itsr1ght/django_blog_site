from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django_distill import distill_path
from . import views

urlpatterns = [
    #distill_path('admin/', admin.site.urls, name="admin"),
    distill_path('about/',views.about_page, name="about"),
    distill_path('',views.home_page, name="home"),
    path('article/', include('article.urls'), name="article")
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
