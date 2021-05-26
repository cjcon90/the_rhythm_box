from django.urls import path
from .views import (
    product_page
)

urlpatterns = [
    path('shop/<slug:category>/<slug:subcategory>/<slug:product>', product_page, name="product_page"),
    path('shop/<slug:category>/<slug:subcategory>/<slug:type>/<slug:product>', product_page, name="product_page"),
]
