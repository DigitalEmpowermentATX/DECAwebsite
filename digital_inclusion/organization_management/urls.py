from django.conf.urls import url
from organization_management import views

app_name = "organization_management"
urlpatterns = [
    url(r'add/$', views.add_organization, name="add"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit_organization, name='edit'),
    url(r'^(?P<pk>[0-9]+)/', views.view_organization, name='view'),    
    url(r'$', views.list_organization, name='index')    
]