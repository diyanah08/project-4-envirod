from django.shortcuts import render,redirect,reverse
from .models import Event

# Create your views here.
def home(request):
    return render(request, 'events/home.template.html')

def browse(request):
    all_events = Event.objects.all()
    return render(request, 'events/browse.template.html', {
        'all_events': all_events
    })

def catalog(request):
    all_events = Event.objects.all()
    return render(request, 'events/catalog.template.html', {
        'all_events': all_events
    })