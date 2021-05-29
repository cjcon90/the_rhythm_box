from django.shortcuts import get_object_or_404, render
from .models import Product, Rating, Review


def product_page(request, category=None, subcategory=None, type=None, product=None):
    product = get_object_or_404(Product, slug=product)
    context = {}
    context['product'] = product
    context['ratings'] = Rating.objects.filter(product=product)
    context['reviews'] = Review.objects.filter(rating__product=product)
    context['rating_options'] = [i * 20 for i in range(1, 6)]
    if request.user.is_authenticated:
        context['user_rating'] = context['ratings'].get(user_id=request.user)
        context['user_review'] = context['reviews'].filter(rating__user_id=request.user)
        print('==================================')
        print(context['user_rating'])
    return render(request, 'products/product_page.html', context)