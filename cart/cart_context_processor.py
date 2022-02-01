from cart.models import Cart, CartItem
from .views import get_cart


def cart_count(request):

    total_items = 0
    try:
        id = get_cart(request)
        cart_id = Cart.objects.get(cart_id=id)
        cart = CartItem.objects.filter(is_active=True, cart=cart_id)

        for item in cart:
            total_items += item.quantity
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        pass
        # print(f'cart_context_processor error {total_items}')

    return {
        'total_items': total_items
    }
