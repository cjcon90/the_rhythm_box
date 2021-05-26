from products.models import Product, Category, Subcategory, Type, Brand
from django.db.models import Q
from django.shortcuts import render

def index(request):
    """
    Landing/Welcome page for website.
    """
    return render(request, 'store/index.html')


def shop(request, category=None, subcategory=None, type=None):
    context = {}
    q = Q()
    if request.GET.get('brand'): # ?brand=*slug
        q &= Q(brand=Brand.objects.get(slug=request.GET.get('brand')).id)
    if type:
        q &= Q(type__slug=type)
    elif subcategory:
        q &= Q(subcategory__slug=subcategory)
    elif category:
        q &= Q(category__slug=category)

    order = request.GET.get('order_by') or '-date_added' # '?order_by=*param'
    
    context['products'] = Product.objects.filter(q).order_by(order)
    return render(request, 'store/shop.html' , context)