from django.shortcuts import render,redirect,reverse
from .models import Event, CreateEvent
from .forms import CreateEventForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'events/home.template.html')
    
def about(request):
    return render(request, 'events/about.template.html')

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
    
def createEvent(request):
    form = CreateEventForm()
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your interest in organising an event. We will contact you shortly to discuss.")
            return render(request, 'events/view_event.template.html')
        else:
            messages.error(request, "Unable to create event. Please try again. Ensure that the date is in a [YYYY-MM-DD] format and the time in a [HH:MM:SS] format")
            return render(request, 'events/create_event.template.html', {
                'form': form
            })
    else:   
        return render(request, 'events/create_event.template.html', {
            'form': form
        })

def editEvent(request, name_id):
    name = CreateEvent.objects.get(pk=name_id)
    
    if request.method == "POST":
        form = CreateEventForm(instance=name)
        form.save()
        return render(request, "edit_event.template name", {
            "form":form
    	})
    else:
        form = CreateEventForm(instance=name)
        return render(request, "edit_event.template name", {
            "form":form
    	})
    	
def viewCreatedEvent(request):
    contents = CreateEvent.objects.all()
    return render(request, 'events/view_event.template.html', {
        'contents':contents
    })