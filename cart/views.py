from django.shortcuts import render, redirect, HttpResponse
from cart.models import CartItem
from pythonium.models import Video
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        messages.add_message(request, messages.WARNING, 'سبد خرید شما خالی است')
        return redirect('/pythonium')
    total_price = 0
    for item in cart_items:
        if item.product.price_off and item.product.price_off > 0:
            item.final_price = item.product.price_off
        else:
            item.final_price = item.product.price
        total_price += item.final_price * item.quantity
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required(login_url='/accounts/login')
def add_to_cart(request, product_id):
    product = Video.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    if created or cart_item.quantity == 0:
        cart_item.quantity += 1
        cart_item.save()
    else:
        messages.add_message(request, messages.INFO, 'محصول در سبد شما موجود است')
    return redirect('cart:view_cart')

@login_required(login_url='/accounts/login')
def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect('cart:view_cart')