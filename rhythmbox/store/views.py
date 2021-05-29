from products.models import Product, Category, Subcategory, Type, Brand
from django.db.models import Q
from django.shortcuts import render
from urllib.parse import urlparse, urlunparse
from django.http import QueryDict
from django.core.paginator import Paginator
from django.db.models import Avg



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
    # if order == 'rating':
    #     products = sorted(Product.objects.filter(q), key= lambda p: p.get_average_rating(), reverse=True)
    # else:
    #     products = Product.objects.filter(q).order_by(order)
    products = Product.objects.filter(q).order_by(order)
    paginator = Paginator(products, 9)
    page_num = request.GET.get('page')
    context['page_obj'] = paginator.get_page(page_num)

    context['categories'] = Category.objects.all()
    context['products'] = products

    return render(request, 'store/shop.html' , context)

