from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Rating, Review
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.safestring import mark_safe
from .forms import ProductRatingForm, ProductReviewForm


def product_page(
    request, category, subcategory, product, type=None
):
    """
    View for handling individual product pages
    """
    product = get_object_or_404(Product, slug=product)
    context = {
        "product": product,
        "ratings": Rating.objects.filter(product=product),
        "reviews": Review.objects.filter(rating__product=product),
        # Create list for looping through star rating options
        "rating_options": [i * 20 for i in range(1, 6)],
    }

    if request.user.is_authenticated:
        # Get user rating for product or None
        try:
            context["user_rating"] = context["ratings"].get(
                user_id=request.user
            )
        except Rating.DoesNotExist:
            context["user_rating"] = None

        # Boolean check if product has been reviewed by User
        context["user_review"] = (
            context["reviews"].filter(rating__user_id=request.user).exists()
        )

    return render(request, "products/product_page.html", context)


@login_required
def rate_product(request, product_id):
    """
    View for adding ratings to products
    using star buttons on product page
    """

    product = Product.objects.get(pk=product_id)
    rating = request.POST.get("star-rating")

    # Update existing rating or create new one
    rating_update_values = {"rating": rating}
    rating_obj, created = Rating.objects.update_or_create(
        user_id=request.user, product=product, defaults=rating_update_values
    )

    # INFO messages redefined as a'star' in settings.py
    messages.info(request, f"Rated {int(rating) // 20} / 5 Stars!")
    return redirect(request.GET.get("next"))


@login_required
def review_product(request, product_slug):
    """
    view for creating or updating product
    reviews, along with associated rating,
    within one single form
    """

    context = {}
    product = Product.objects.get(slug=product_slug)
    context["product"] = product

    # Check if user has already rated and/or already reviewed this product
    already_rated = Rating.objects.filter(
        user_id=request.user, product__slug=product_slug
    ).exists()
    already_reviewed = Review.objects.filter(
        rating__user_id=request.user, rating__product__slug=product_slug
    ).exists()

    if request.POST:
        rating_form = ProductRatingForm(request.POST)
        review_form = ProductReviewForm(request.POST)

        if rating_form.is_valid() and review_form.is_valid():
            # Get form data
            rating = rating_form.cleaned_data["rating"]
            headline = review_form.cleaned_data["headline"]
            content = review_form.cleaned_data["content"]

            # Create rating or update if exists
            rating_update_values = {"rating": rating}
            rating_obj, created = Rating.objects.update_or_create(
                user_id=request.user,
                product=product,
                defaults=rating_update_values,
            )

            # Create review, or update if exists
            review_update_values = {"headline": headline, "content": content}
            review_obj, created = Review.objects.update_or_create(
                rating=rating_obj, defaults=review_update_values
            )

            messages.info(request, f"Review submitted!")
            return redirect(product.get_product_url())
        else:
            context["rating_form"] = rating_form
            context["review_form"] = review_form

    # GET request
    else:
        # Prepopulate rating if user has already rated
        if already_rated:
            prev_rating = Rating.objects.get(
                user_id=request.user, product__slug=product_slug
            )
            context["rating_form"] = ProductRatingForm(
                initial={"rating": prev_rating.rating}
            )
        else:
            context["rating_form"] = ProductRatingForm()

        # Prepopulate review if user has already reviewed
        if already_reviewed:
            prev_review = Review.objects.get(rating=prev_rating)
            context["review_form"] = ProductReviewForm(
                initial={
                    "headline": prev_review.headline,
                    "content": prev_review.content,
                }
            )
        else:
            context["review_form"] = ProductReviewForm()

    return render(request, "products/review_product.html", context)
