from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about_page),
    path('',views.home_page),
    path('article/', include('article.urls'))
]

urlpatterns += staticfiles_urlpatterns()