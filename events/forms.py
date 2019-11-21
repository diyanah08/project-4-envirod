from django import forms
from .models import CreateEvent

class CreateEventForm(forms.ModelForm):

    class Meta:
        model = CreateEvent
        fields = (
            'name', 'phone_number', 'event_title', 'description', 'cost_per_pax', 'seats', 'date', 'start_time', 'hours_needed', 'location', 'tags'
        )
    
    date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%y'),
        input_formats=('%d/%m/%y', )
        )
        
    start_time = forms.TimeField(
        widget=forms.TimeInput(format='%I.%M%p'),
        input_formats=('%I.%M%p', )
        )