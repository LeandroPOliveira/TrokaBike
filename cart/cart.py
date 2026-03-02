import json
from products.models import Product
from users.models import Profile


class Cart:
    SESSION_KEY = "cart"

    def __init__(self, request):
        self.session = request.session
        self.request = request

        cart = self.session.get(self.SESSION_KEY)

        if not cart:
            cart = self.session[self.SESSION_KEY] = {}

        self.cart = cart

    # -------------------------
    # Core Methods
    # -------------------------

    def add(self, product, quantity=1):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = int(quantity)
        else:
            self.cart[product_id] += int(quantity)

        self._save()

    def remove(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]

        self._save()

    def update(self, product_id, quantity):
        product_id = str(product_id)
        self.cart[product_id] = int(quantity)

        self._save()

    def clear(self):
        self.session[self.SESSION_KEY] = {}
        self._save()

    # -------------------------
    # Utility Methods
    # -------------------------

    def __len__(self):
        return sum(self.cart.values())

    def get_products(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_total_price(self):
        products = self.get_products()
        total = 0

        for product in products:
            total += product.price * self.cart[str(product.id)]

        return total

    def get_cart_items(self):
        products = self.get_products()
        items = []

        for product in products:
            quantity = self.cart[str(product.id)]
            subtotal = product.price * quantity

            items.append({
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal,
            })

        return items

    # -------------------------
    # Internal Methods
    # -------------------------

    def _save(self):
        self.session.modified = True

        if self.request.user.is_authenticated:
            self._save_cart_to_profile()

    def _save_cart_to_profile(self):
        profile = Profile.objects.filter(user=self.request.user).first()

        if profile:
            profile.old_cart = json.dumps(self.cart)
            profile.save()