from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    for product in products:
        quantity = cart[str(product.id)]
        total_price = product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity, 'total': total_price})
    return render(request, 'cart.html', {'cart': cart_items})

@login_required(login_url='login')

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('product_list')

    order = Order.objects.create(user=request.user)
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        OrderItem.objects.create(
            order=order,
            product_name=product.name,
            quantity=quantity,
            price=product.price,
        )
    request.session['cart'] = {}
    print("dfdgdfgdfgdf",order)
    order_items = order.orderitem_set.all()

    return render(request, 'checkout.html', {
        'order': order,
        'order_items': order_items
    })
