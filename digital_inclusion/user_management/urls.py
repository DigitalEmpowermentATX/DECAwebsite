from django.conf.urls import url
from django.contrib.auth import views as auth_views
from user_management import views
urlpatterns = [
    url(r'login/$', auth_views.login, {'template_name': 'login.jinja2'} ,name='login' ),
    url(r'logout/$', auth_views.logout, name='logout'),
    url(r'register/$', views.register, name='register'),
]