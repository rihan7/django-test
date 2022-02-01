from django.urls.conf import path
from . import views


urlpatterns = [
    path('', views.Store.as_view(), name='store'),
    path('search/', views.Search.as_view(), name='search'),
    path('<slug:category_slug>', views.Store.as_view(), name='category_view'),
    path('<slug:category_slug>/<slug:product_slug>',
         views.Product_detail.as_view(), name='product_view'),

]
