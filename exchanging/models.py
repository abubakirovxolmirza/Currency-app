from django.db import models
from django.utils import timezone

# Create your models here.

class Currency(models.Model):
    to_money = models.CharField(max_length=5)
    from_money = models.CharField(max_length=5)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    converted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.datetime.now)


    def __str__(self):
        return f"{self.amount} qiymatdagi pulni {self.from_money}dan {self.to_money}ga o'girdi natija esa {self.converted_amount}"

