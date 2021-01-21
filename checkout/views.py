from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from cart.contexts import cart_contents


def checkout(request):
    # Handle payments
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I7NK4KoPZu7CLweV1wgnes3jYF55dV0xuakNDWZlSVU0chYVLuOoJTExyBydTY4bgMW8hQR7oYFy90PXt4t2oZw00Kw5cDods',
        'client_secret': "testetstts",
    }

    return render(request, template, context)
