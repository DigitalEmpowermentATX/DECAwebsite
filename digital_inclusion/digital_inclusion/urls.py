"""digital_inclusion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from organization_management import views
from main import urls as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("org/", include('organization_management.urls', namespace='orgs')),
    path("accounts/", include('user_management.urls')),
    path("flag/", include('flagging.urls', namespace='flags')),
    path("events/", include('events.urls', namespace='events')),
    path("search/", include('search.urls', namespace='search')),
] + main_urls.urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
