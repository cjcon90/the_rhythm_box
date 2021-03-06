from django.urls import path

from .views import product_page, rate_product, review_product, delete_review

urlpatterns = [
    path(
        "shop/<slug:category>/<slug:subcategory>/<slug:product>",
        product_page,
        name="product_page",
    ),
    path(
        "shop/<slug:category>/<slug:subcategory>/<slug:type>/<slug:product>",
        product_page,
        name="product_page",
    ),
    path("rate/<int:product_id>/", rate_product, name="rate_product"),
    path("review/<slug:product_slug>/", review_product, name="review_product"),
    path(
        "review/delete/<int:review_id>/", delete_review, name="delete_review"
    ),
]
