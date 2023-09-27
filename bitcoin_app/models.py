from django.db import models

class BitcoinPrice(models.Model):
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - ${self.price}"
