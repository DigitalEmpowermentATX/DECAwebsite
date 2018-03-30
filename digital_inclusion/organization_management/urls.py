from django.conf.urls import url
from organization_management import views

urlpatterns = [
    url(r'add/$', views.add_organization),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit_organization, name='edit_organization'),
    url(r'^(?P<pk>[0-9]+)/flag/$', views.flag_organization, name='flag_organization'),
    url(r'^(?P<pk>[0-9]+)/', views.view_organization, name='view_organization'),    
    url(r'$', views.list_organization)    
]