from django.shortcuts import get_object_or_404, render
from .models import Product

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {}
    context['product'] = product

    return render(request, 'products/item.html', context)