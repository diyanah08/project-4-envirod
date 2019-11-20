from django.urls import path, include
from .views import login, logout, register, profile, editProfile
from payment.views import events_history

urlpatterns = [
    path('login/', login, name ="login"),
    path('logout/', logout, name ="logout"),
    path('register/', register, name ="register"),
    path('profile/', profile, name ="profile"),
    path('edit/', editProfile, name ="editProfile"),
    path('events_history/', events_history, name ="event_history"),
]
