from django.conf.urls import url
from flagging import views
from django.http import HttpRequest

app_name = "flagging"
urlpatterns = [
    url(r'submit/$', views.flag, name="flag"),
]