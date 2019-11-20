from django.urls import path, include
from .views import catalog, browse, home, createEvent, editEvent, viewCreatedEvent

urlpatterns = [
    path('', home, name ="home"),
    path('catalog/', catalog, name ="catalog"),
    path('browse/', browse, name="browse"),
    path('create/', createEvent, name ="create_event"),
    path('edit_event/<content_id>', editEvent, name ="edit_event"),
    path('view_created_event/', viewCreatedEvent, name="view_created_event")
]