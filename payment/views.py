from django.shortcuts import render, HttpResponse
from .forms import OrderForm, PaymentForm
from .models import Transaction, Charge, LineItem
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from cart.models import CartItem
import stripe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def calculate_cart_cost(request):
    all_cart_items = CartItem.objects.filter(owner=request.user)
    amount = 0
    for cart_item in all_cart_items:
        amount += cart_item.event.cost * cart_item.quantity
        
    return amount

# Create your views here.
def payment_form(request):
    total_cost = calculate_cart_cost(request)
    all_cart_items = CartItem.objects.filter(owner=request.user)
        
    return render(request, 'payment/payment_form.template.html', {
        'total_cost':total_cost/100,
        'all_cart_items':all_cart_items
    })
    
def pay(request):
    amount = calculate_cart_cost(request)
    
    if request.method == 'GET':

        transaction = Transaction()
        transaction.owner = request.user
        transaction.cart_items = CartItem.objects.filter(owner=request.user)
        transaction.status = "pending"
        transaction.date = timezone.now()
        transaction.save()
        
        all_cart_items = CartItem.objects.filter(owner=request.user)
        for cart_item in all_cart_items:
        	lineItem = LineItem()
        	lineItem.transaction = transaction
        	lineItem.event = cart_item.event
        	lineItem.name = cart_item.event.name
        	lineItem.sku = cart_item.event.sku
        	lineItem.cost = cart_item.event.cost
        	lineItem.owner = request.user
        	lineItem.save()

        order_form = OrderForm()
        
        payment_form = PaymentForm()
        return render(request, 'payment/pay.template.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            'amount' : amount,
            'transaction': transaction,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
        })
        
    else:
    
        transaction_id = request.POST['transaction_id']
        transaction = Transaction.objects.get(pk=transaction_id)
        # if transaction.status == 'pending':
        # 	return HttpResponse("session has expired")

        
        stripeToken = request.POST['stripe_id']
        
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount= int(request.POST['amount']),
                    currency='sgd',
                    description='Payment',
                    card=stripeToken
                    )
                    
                if customer.paid:
                    
                    order = order_form.save(commit=False)
                    order.date=timezone.now()
                    order.save()
                    
                    transaction.status = 'approved'
                    transaction.charge = order
                    transaction.save()
                    
                    line_items = LineItem.objects.filter(transaction_id=transaction.id)
                    for each_line_item in line_items:
                        each_line_item.event.quantity -= 1
                        each_line_item.event.save()
                        
                    cart_items = CartItem.objects.filter(owner=request.user).delete()
                    
                    return render(request, 'payment/thankyou.template.html')
                else:
                    messages.error(request, "Your card has been declined")
            except stripe.error.CardError:
                    messages.error(request, "Your card has been declined!")
            
        else:
             return render(request, 'payment/pay.template.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            'amount' : amount,
            'transaction': transaction,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
        })
        
        return render(request, 'payment/pay.template.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            'amount' : amount,
            'transaction': transaction,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
            })
            
def events_history(request):
    line_items = LineItem.objects.filter(owner=request.user)
    
    paginator = Paginator(line_items, 3)

    page = request.GET.get('page')
    try:
        line_items = paginator.page(page)
    except PageNotAnInteger:
        line_items = paginator.page(1)
    except EmptyPage:
        line_items = paginator.page(paginator.num_pages)
    
    return render(request, 'accounts/history.template.html', {
        'line_items' : line_items
    })