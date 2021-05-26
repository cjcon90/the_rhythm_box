from products.models import Product, Category
from django.shortcuts import render

def index(request):
    """
    Landing/Welcome page for website.
    """
    return render(request, 'store/index.html')


def shop(request):
    context = {}
    lookup = {'category__in': range(0, 100)}
    # lookup = {'subcategories': True}
    context['products'] = Product.objects.filter(**lookup).all()
    context['categories'] = Category.objects.all()
    context['test'] = Product.objects.filter(**lookup)
    return render(request, 'store/shop.html' , context)