from decimal import Decimal


# Contexts class to save to contents of the shopping cart
def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    delivery = Decimal(5.99)

    # Only add delivery costs when items are in the shopping cart
    if total == 0:
        grand_total = total
    else:
        grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
