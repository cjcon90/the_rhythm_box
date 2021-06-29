from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404

from products.models import Product


def cart_detail(request):
    """
    view for showing items currently in user cart
    """
    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """
    view for adding an item to user cart
    """
    quantity_select = request.POST.get("quantity")
    quantity = 1 if quantity_select is None else int(quantity_select)
    redirect_url = request.POST.get("redirect_url")

    cart = request.session.get("cart", {})
    product = get_object_or_404(Product, pk=item_id)
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session["cart"] = cart
    messages.success(request, f"{product.title} (x{quantity}) added to cart!")
    return redirect("cart")


def update_cart(request, item_id):
    """
    Adjust quantity of items in shopping cart
    """

    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session["cart"] = cart
    messages.success(request, f"Shopping cart updated")
    return redirect("cart")


def remove_cart_item(request, item_id):
    """
    Adjust quantity of items in shopping cart
    """

    cart = request.session.get("cart", {})
    product = get_object_or_404(Product, pk=item_id)

    cart.pop(item_id)

    request.session["cart"] = cart
    messages.success(request, f"{product.title} removed from cart")
    return redirect("cart")
