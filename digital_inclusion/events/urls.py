from django.conf.urls import url
from events import views
from django.http import HttpRequest

app_name = "events"
urlpatterns = [
    url(r'add/$', views.add, name="add_event"),
    url(r'$', views.calendar, name="calendar"),
]