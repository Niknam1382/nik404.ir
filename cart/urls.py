from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('detail/', views.cart_detail, name='cart_detail'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]