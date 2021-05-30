from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Rating, Review
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.safestring import mark_safe


def product_page(request, category=None, subcategory=None, type=None,
                 product=None):
    """
    View for handling individual product pages
    """
    product = get_object_or_404(Product, slug=product)
    context = {'product': product,
               'ratings': Rating.objects.filter(product=product),
               'reviews': Review.objects.filter(rating__product=product),
               'rating_options': [i * 20 for i in range(1, 6)]}
    # Create list for looping through star rating options
    if request.user.is_authenticated:
        try:
            # Check if product has already been rated by current user
            context['user_rating'] = context['ratings'].get(
                user_id=request.user)
        except Rating.DoesNotExist:
            context['user_rating'] = None
        context['user_review'] = context['reviews'].filter(
            rating__user_id=request.user).exists()
    return render(request, 'products/product_page.html', context)


@login_required
def rate_product(request, product_id):
    """
    View for adding ratings to products
    using star buttons on product page
    """
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
    messages.info(request, f'Rated {int(rating) // 20} / 5 Stars!')
    return redirect(request.GET.get('next'))
