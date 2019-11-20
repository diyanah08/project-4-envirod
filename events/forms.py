from django import forms
from .models import CreateEvent

class CreateEventForm(forms.ModelForm):

    class Meta:
        model = CreateEvent
        fields = (
            'name', 'phone_number', 'event_title', 'description', 'cost', 'seats', 'date', 'start_time', 'hours_needed', 'location', 'tags'
        )