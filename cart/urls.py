from django.urls import path
from .views import cart_detail, add_to_cart, update_cart, remove_cart_item

urlpatterns = [
    path("cart/", cart_detail, name="cart"),
    path("cart/add/<item_id>/", add_to_cart, name="add_to_cart"),
    path("cart/update/<item_id>/", update_cart, name="update_cart"),
    path("cart/remove/<item_id>/", remove_cart_item, name="remove_cart_item"),
]
