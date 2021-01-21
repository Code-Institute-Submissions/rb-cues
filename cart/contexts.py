from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product


# Contexts class to save to contents of the shopping cart
def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    product_total = 0
    delivery = Decimal(5.99)
    cart = request.session.get('cart', {})

    # Calculate totals and fill cart_items
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        product_total = quantity * product.price

        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'product_total': product_total,
        })

    # Only add delivery costs when items are in the shopping cart
    if total == 0:
        grand_total = total
    else:
        grand_total = delivery + total

    # Shopping cart contents
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
