from django.shortcuts import render, redirect
from .forms import OrderForm
from django.conf import settings

def checkout(request):
    context = {}
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')
    context['order_form'] = OrderForm()
    context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
    context['client_secret'] = 'shhhhh this is a secret'
    return render(request, 'checkout/checkout.html', context)
