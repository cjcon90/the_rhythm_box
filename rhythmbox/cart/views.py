from django.shortcuts import render, redirect


def cart_detail(request):
    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):

    quantity_select = request.POST.get("quantity")
    quantity = 1 if quantity_select is None else int(quantity_select)
    redirect_url = request.POST.get("redirect_url")

    cart = request.session.get("cart", {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session["cart"] = cart
    return redirect('cart')
