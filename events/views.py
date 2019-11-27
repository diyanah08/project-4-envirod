from django.shortcuts import render,redirect,reverse
from .models import Event, CreateEvent
from .forms import CreateEventForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import filters
from .filters import EventFilter

# Create your views here.
def home(request):
    return render(request, 'events/home.template.html')
    
def about(request):
    return render(request, 'events/about.template.html')


# before login view of events
def browse(request):
    all_events = Event.objects.all()
    event_filter = EventFilter(request.GET, queryset=all_events)
    filtered_qs = filters.EventFilter(
                      request.GET, 
                      queryset=all_events
                  ).qs
    
    paginator = Paginator(filtered_qs, 3)

    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    
    return render(request, 'events/browse.template.html', {
        'paginator': paginator,
        'filter': event_filter,
        'filtered': filtered_qs,
        'response' : response
    })

# after login view of events
def catalog(request):
    all_events = Event.objects.all()
    event_filter = EventFilter(request.GET, queryset=all_events)
    filtered_qs = filters.EventFilter(
                      request.GET, 
                      queryset=all_events
                  ).qs
    
    paginator = Paginator(filtered_qs, 3)

    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    
    return render(request, 'events/catalog.template.html', {
        'paginator': paginator,
        'filter': event_filter,
        'filtered': filtered_qs,
        'response' : response
    })

# form for enquiring to request to use EnviroD space for an event
@login_required
def createEvent(request):
    form = CreateEventForm()
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your interest in organising an event. We will contact you shortly to discuss.")
            return redirect(reverse('view_created_events'))
        else:
            messages.error(request, "Unable to create event. Please try again. Ensure that the date is in a [DD/MM/YY] format and the time in a [3.30pm] format")
            return render(request, 'events/create_event.template.html', {
                'form': form
            })
    else:   
        return render(request, 'events/create_event.template.html', {
            'form': form
        })

# view above requests
@login_required
def viewCreatedEvents(request):

    createdEvents = CreateEvent.objects.all().order_by('date')
    
    paginator = Paginator(createdEvents, 3)

    page = request.GET.get('page')
    try:
        createdEvents = paginator.page(page)
    except PageNotAnInteger:
        createdEvents = paginator.page(1)
    except EmptyPage:
        createdEvents = paginator.page(paginator.num_pages)

    return render(request, "events/view_event.template.html", {"createdEvents": createdEvents})

# edit requests
@login_required
def editEvent(request, create_event_id):
    event = get_object_or_404(CreateEvent, pk=create_event_id)
    
    if request.method == "POST":
        form = CreateEventForm(request.POST, instance=event)
        if form.is_valid():
            update = form.save(commit=False)
            
            update.save()
            
            return redirect(reverse('view_created_events'))
    else:
        form = CreateEventForm(instance=event)
        return render(request, "events/edit_event.template.html", {
            "form":form
    	})

# delete requests
@login_required
def deleteEvent(request, create_event_id):
    event = get_object_or_404(CreateEvent, pk=create_event_id)
    event.delete()
    messages.success(request, "Event Deleted")
    return redirect(reverse('view_created_events'))