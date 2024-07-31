from django.db import models
from pythonium.models import Video
from django.core.validators import MaxValueValidator

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Video, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(1)])

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
