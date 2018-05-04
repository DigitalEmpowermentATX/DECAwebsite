from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'about/$', views.about, name="about"),
    url(r'map/$', views.map, name="map"),
    url(r'^$', views.index, name="index"),
]