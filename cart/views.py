from django.shortcuts import render,redirect,reverse
from .models import CartItem
from events.models import Event

def view_cart(request):
    all_cart_items = CartItem.objects.filter(owner=request.user)
    return render(request, 'cart/cart.template.html',{
        'all_cart_items':all_cart_items
    })

def add_to_cart(request, event_id):
    
    event = Event.objects.get(pk=event_id)
    
    existing_cart_item = CartItem.objects.filter(owner=request.user, event=event).first()
    
    if existing_cart_item == None:
        new_cart_item = CartItem()
        new_cart_item.event = event
        new_cart_item.owner = request.user
        new_cart_item.quantity = 1
        new_cart_item.save()
    else:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    
    all_events = Event.objects.all()
    return render(request, 'events/added.template.html', {
        'all_events': all_events
    })
    
def remove_from_cart(request, cart_item_id):

    existing_cart_item = CartItem.objects.get(pk=cart_item_id)
    if existing_cart_item.quantity == 1:
        existing_cart_item.delete()
    else:
        existing_cart_item.quantity -= 1
        existing_cart_item.save()
    return redirect(reverse('view'))