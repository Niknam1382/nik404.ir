from django.db import models
from django.contrib.auth.models import User
from pythonium.models import Video

class CartItem(models.Model):
    product = models.ForeignKey(Video, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    # final_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # def save(self, *args, **kwargs):
    #     if self.product.price_off and self.product.price_off > 0:
    #         self.final_price = self.product.price_off
    #     else:
    #         self.final_price = self.product.price
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.quantity} x {self.product}'