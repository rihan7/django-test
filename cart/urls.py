from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.Cart_View.as_view(), name='cart'),
    path('add_to_cart/<product_id>',
         views.Add_to_cart.as_view(), name='add_to_cart'),
    path('sub_to_cart/<product_id>', views.Sub_to_cart.as_view(), name="sub_cart"),
    path('remove_cart/<product_id>',
         views.remove_cart.as_view(), name="remove_cart")
]
