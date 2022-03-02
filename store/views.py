from cart.models import Cart, CartItem
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from store.models import Product
from categories.models import Categories
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


class Store(View):

    def get(self, request, category_slug=None):
        category = None
        products = None

        if category_slug:
            category = get_object_or_404(Categories, slug=category_slug)
            products = Product.objects.all().filter(is_available=True, categories=category)
        else:
            products = Product.objects.all().filter(is_available=True)

        # print(request.GET.get('page'))

        page = request.GET.get('page')

        p = Paginator(products, 2).get_page(page)

        context = {
            'products': p,
            'total_product': products.count()
        }

        return render(request, 'store.html', context)


class Product_detail(View):

    def get(self, request, category_slug, product_slug):
        category = get_object_or_404(Categories, slug=category_slug)
        product = Product.objects.get(
            is_available=True, categories=category, slug=product_slug)

        try:
            cart = Cart.objects.get(cart_id=request.session.session_key)
            in_cart = CartItem.objects.filter(
                cart=cart, product=product, is_active=True).exists()
        except:
            in_cart = False

        return render(request, 'product_detail.html', {'product': product, 'in_cart': in_cart})


class Search(View):

    def get(self, request):

        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)).order_by('created_at')

        context = {
            'products': products,
            'total_product': products.count()
        }

        return render(request, 'store.html', context)
