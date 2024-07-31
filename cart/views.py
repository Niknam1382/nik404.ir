from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart, CartItem
from pythonium.models import Video
from django.contrib import messages

def product_list(request):
    products = Video.objects.all()
    return render(request, 'cart/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Video, id=product_id)
    cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id'))
    request.session['cart_id'] = cart.id
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        if cart_item.quantity == 0:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.add_message(request, messages.INFO, "این محصول در سبد خرید شما وجود دارد")
    return redirect('/cart/detail')

def cart_detail(request):
    cart = Cart.objects.get(id=request.session.get('cart_id'))
    c = CartItem.objects.all().count()
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'c': c})

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('/cart/detail')
