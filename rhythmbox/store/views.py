from products.models import Product
from django.shortcuts import render

def index(request):
    """
    Landing/Welcome page for website.
    """
    return render(request, 'store/index.html')


def shop(request):
    products = Product.objects.all()
    context = {}
    context['products'] = products
    return render(request, 'store/shop.html' , context)