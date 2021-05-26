from django.urls import path
from .views import (
    product_detail
)

urlpatterns = [
    path('item/<str:slug>', product_detail, name="product_detail")
]
