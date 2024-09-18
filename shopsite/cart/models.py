from django.db import models
from product.models import product

# Create your models here.

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)

    def get_total_price(self):
       try:
        return sum(item.get_total_price() for item in self.items.all())
       except Exception as e:
        # Handle the error and provide a user-friendly error message
        print(f"An error occurred: {e}")
        return 0  # or some other default value

class Item(models.Model):
    cart = models.ForeignKey(Cart,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(product,related_name='cart_product',on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity