from django.conf.urls import url
from django.http import HttpRequest
import search.views

app_name = "search"
urlpatterns = [
    url(r'autocomplete/$', search.views.autocomplete, name="autocomplete"),
    url(r'^$', search.views.search, name="search"),
]