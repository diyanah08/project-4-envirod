from .models import Event
import django_filters

class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Event
        fields = ['name', 'location', 'tags' ]