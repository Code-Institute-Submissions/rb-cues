from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I7NK4KoPZu7CLweV1wgnes3jYF55dV0xuakNDWZlSVU0chYVLuOoJTExyBydTY4bgMW8hQR7oYFy90PXt4t2oZw00Kw5cDods',
        'client_secret': "testetstts",
    }

    return render(request, template, context)
