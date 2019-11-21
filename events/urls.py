from django.urls import path, include
from .views import catalog, browse, home, createEvent, viewCreatedEvents, editEvent, deleteEvent

urlpatterns = [
    path('', home, name ="home"),
    path('catalog/', catalog, name ="catalog"),
    path('browse/', browse, name="browse"),
    path('create/', createEvent, name ="create_event"),
    path('view_created_events/', viewCreatedEvents, name="view_created_events"),
    path('edit_event/<create_event_id>', editEvent, name ="edit_event"),
    path('delete_event/<create_event_id>', deleteEvent, name = "delete_event")
]