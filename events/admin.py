from django.contrib import admin
from .models import Event, Location, Tag, CreateEvent

# Register your models here.
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Tag)
admin.site.register(CreateEvent)