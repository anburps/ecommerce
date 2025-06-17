from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem
from django.contrib.auth.decorators import login_required

def product_list(request):

    cart = request.session.get('cart', {})

    total_quantity = sum(cart.values())
    context = {
        'products': Product.objects.all(),
        'cart_qty': total_quantity
    }
    return render(request, 'product_list.html', context)

def add_to_cart(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    cart[product_id_str] = cart.get(product_id_str, 0) + quantity
    request.session['cart'] = cart

    total_quantity = sum(cart.values())
    request.session['cart_count'] = total_quantity  

    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    items = []

    for product_id, quantity in cart.items():
        if quantity > 0:
            product = Product.objects.get(id=product_id)
            items.append({
                'product': product,
                'quantity': quantity,
                'total': quantity * product.price
            })

    context = {
        'cart_items': items,
        'cart_count': sum(cart.values())
    }
    return render(request, 'cart.html', context)

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

