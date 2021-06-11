from django.shortcuts import render, redirect
from .forms import OrderForm

def checkout(request):
    context = {}
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')
    context['order_form'] = OrderForm()
    return render(request, 'checkout/checkout.html', context)
