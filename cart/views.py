from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """
    A view that renders the shopping cart page
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add a quantity of the
    product to the shopping cart
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        # Add a item to the shopping cart which is allreade in there
        cart[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}'
        )
    else:
        # Add a new item to the shopping cart
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)
