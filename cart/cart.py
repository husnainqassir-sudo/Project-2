from store.models import Product

class Cart():

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')

        if 'cart' not in self.session:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'price': str(product.price),
                'quantity': quantity
            }
        else:
            self.cart[product_id]['quantity'] += quantity

        self.session.modified = True

    def __len__(self):
        return sum(item.get("quantity", 1) for item in self.cart.values())
    def get_prods(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_quants(self):
        return self.cart

    def update(self, product, quantity):
        product = str(product)

        if product in self.cart:
            self.cart[product]['quantity'] = quantity
            self.session.modified = True

def delete(self, product):
    product_id = str(product)

    if product_id in self.cart:
        del self.cart[product_id]
        self.session.modified = True