from .models import Event
import django_filters

class EventFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Event
        fields = ['description', 'location', 'tags' ]