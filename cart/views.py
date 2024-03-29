from genericpath import exists
from django.http.response import HttpResponse
from cart.models import Cart, CartItem
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from store.models import Product, Variation

# Create your views here.


class Cart_View(View):

    def get(self, request):
        cart = None
        cart_items = None
        total_price = 0

        try:
            cart = Cart.objects.get(cart_id=request.session.session_key)
            cart_items = CartItem.objects.all().filter(cart=cart)
            for item in cart_items:

                total_price += item.subtotal()
        except Cart.DoesNotExist:
            return HttpResponse('Cart Not Found')
        except CartItem.DoesNotExist:
            return HttpResponse('CartItem Not Found')

        taxes = (5*total_price)/100
        total = total_price + taxes

        context = {
            'items': cart_items,
            'total_price': total_price,
            'taxes': taxes,
            'total': total
        }

        return render(request, 'cart.html', context)


def get_cart(request):
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    return session_id


class Add_to_cart(View):

    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            variations = Variation.objects.filter(
                product=product)

            product_variations = []

            for item in request.GET:
                key = item
                value = request.GET[item]
                variation = variations.get(
                    variation_category__iexact=key, variation_value__iexact=value)
                product_variations.append(variation)

            cart = get_cart(request)

            # get or create cart
            try:
                cart = Cart.objects.get(cart_id=cart)
            except Cart.DoesNotExist:
                cart = Cart(cart_id=cart)
                cart.save()

            cart_items = CartItem.objects.filter(
                cart=cart, product=product)

            ## if cart exists => item exists in cart items-> increase || item not in cart -> create
            if cart_items.exists():
                is_exist = False
                for item in cart_items:
                    v = item.variations.all()
                    if all(pv in v for pv in product_variations):
                        item.quantity += 1
                        item.save()
                        is_exist = True
                        break

                if not is_exist:
                    cart_item = CartItem.objects.create(cart=cart, product=product,
                                                        quantity=1)
                    cart_item.variations.set(product_variations)

            else:
                cart_item = CartItem.objects.create(cart=cart, product=product,
                                                    quantity=1)
                cart_item.variations.set(product_variations)

        except Exception as error:
            print(error)

        return redirect('/cart')


class Sub_to_cart(View):

    def get(self, request, item_id):

        # cart = Cart.objects.get(cart_id=request.session.session_key)
        # product = Product.objects.get(id=product_id)
        # cart_item = CartItem.objects.get(
        #     cart=cart, product=product, is_active=True)
        
        cart_item = CartItem.objects.get(id=item_id, cart__cart_id=request.session.session_key)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

        return redirect('/cart')


class remove_cart(View):

    def get(self, request, item_id):
        # cart = Cart.objects.get(cart_id=request.session.session_key)
        # product = Product.objects.get(id=product_id)
        # cart_item = CartItem.objects.get(
        #     cart=cart, product=product, is_active=True)
        # cart_item.delete()
        
        cart_item = CartItem.objects.get(id=item_id, cart__cart_id=request.session.session_key).delete()
        print(cart_item)

        return redirect('/cart')
