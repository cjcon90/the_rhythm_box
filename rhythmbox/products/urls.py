from django.urls import path
from .views import (
    product_page,
    rate_product,
)

urlpatterns = [
    path(
        'shop/<slug:category>/<slug:subcategory>/<slug:product>', product_page,
        name="product_page"),
    path(
        'shop/<slug:category>/<slug:subcategory>/<slug:type>/<slug:product>',
        product_page, name="product_page"),
    path(
        'rate/<int:product_id>', rate_product, name="rate_product")
]
