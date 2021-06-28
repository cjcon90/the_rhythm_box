from products.models import Product, Category, Brand
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator


def index(request):
    """
    Landing/Welcome page for website.
    """
    return render(request, "store/index.html")


def shop(request, category=None, subcategory=None, type=None):
    """
    Main shop page page list of available products
    """

    context = {}
    q = Q()

    # brand and text search
    if "brand" in request.GET:
        query = request.GET.get("brand")
        q &= Q(brand__name__iexact=query)
    elif "q" in request.GET:
        query = request.GET.get("q")
        q &= (
            Q(title__icontains=query)
            | Q(category__title__icontains=query)
            | Q(subcategory__title__icontains=query)
            | Q(type__title__icontains=query)
            | Q(brand__name__icontains=query)
        )

    # URL parameter filters
    if type:
        q &= Q(type__slug=type)
    elif subcategory:
        q &= Q(subcategory__slug=subcategory)
    elif category:
        q &= Q(category__slug=category)

    # product display ordering
    order = request.GET.get("order_by") or "-date_added"  # '?order_by=*param'
    if order == "rating":
        products = sorted(
            Product.objects.filter(q),
            key=lambda p: p.get_average_rating(),
            reverse=True,
        )
    else:
        products = Product.objects.filter(q).order_by(order)

    # Pagination object
    paginator = Paginator(products, 9)
    page_num = request.GET.get("page")
    context["page_obj"] = paginator.get_page(page_num)

    # Product List
    context["products"] = products

    return render(request, "store/shop.html", context)
