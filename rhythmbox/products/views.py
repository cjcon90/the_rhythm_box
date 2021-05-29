from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Rating, Review
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.http import is_safe_url



def product_page(request, category=None, subcategory=None, type=None, product=None):
    '''
    View for handling individual product pages
    '''
    product = get_object_or_404(Product, slug=product)
    context = {}
    context['product'] = product
    context['ratings'] = Rating.objects.filter(product=product)
    context['reviews'] = Review.objects.filter(rating__product=product)
    # Create list for looping through star rating options
    context['rating_options'] = [i * 20 for i in range(1, 6)]
    if request.user.is_authenticated:
        try:
            # Check if product has already been rated by current user
            context['user_rating'] = context['ratings'].get(user_id=request.user)
        except Rating.DoesNotExist:
            context['user_rating'] = None
        context['user_review'] = context['reviews'].filter(rating__user_id=request.user).exists()
    return render(request, 'products/product_page.html', context)


@login_required
def rate_product(request, product_id):
    '''
    View for adding ratings to products
    using star buttons on product page
    '''
    product = Product.objects.get(pk=product_id)
    rating = request.POST.get('star-rating')
    try:
        r = Rating.objects.get(user_id=request.user, product=product)
    except Rating.DoesNotExist:
        r = Rating(user_id=request.user, product=product)
    finally:
        r.rating = rating
        r.save()
    # TODO: create success message
    return redirect(request.GET.get('next'))