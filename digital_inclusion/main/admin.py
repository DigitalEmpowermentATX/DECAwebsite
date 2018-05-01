from django.contrib import admin
from events.models import Event
from main.models import UIComponent
# Register your models here.
admin.site.register(Event)
admin.site.register(UIComponent)