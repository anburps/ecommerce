class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})

    def add(self, product_id, price):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'price': str(price)}
        else:
            self.cart[product_id]['quantity'] += 1
        self.session['cart'] = self.cart
        self.session.modified = True

    def items(self):
        from .models import Product
        products = Product.objects.filter(id__in=self.cart.keys())
        for p in products:
            item = self.cart[str(p.id)]
            yield {
                'product': p,
                'quantity': item['quantity'],
                'total': float(item['price']) * item['quantity']
            }

    def total_price(self):
        return sum(float(i['price']) * i['quantity'] for i in self.cart.values())
