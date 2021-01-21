from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
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


def adjust_cart(request, item_id):
    """
    Adjust the quantity of a
    product to the specified amount
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        if cart[item_id] < quantity:
            messages.info(
                request, f'Updated {product.name} quantity to {quantity}'
            )
        else:
            messages.info(
                request, f'Removed {product.name} quantity to {quantity}'
            )

        cart[item_id] = quantity
    else:
        cart.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from your cart'
        )

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Remove the product from the shopping cart
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
