from django.shortcuts import get_object_or_404, render
from .models import Product, Rating, Review


def product_page(request, category=None, subcategory=None, type=None, product=None):
    product = get_object_or_404(Product, slug=product)
    context = {}
    context['product'] = product
    context['reviews'] = Review.objects.filter(rating__product=product)
    if request.user.is_authenticated:
        context['my_review'] = context['reviews'].filter(rating__user_id=request.user)
    return render(request, 'products/product_page.html', context)