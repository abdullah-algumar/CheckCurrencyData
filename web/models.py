from django.db import models
from utils.models import BaseModel


class Coin(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    buying = models.FloatField()
    buyingstr = models.CharField(max_length=100)
    selling = models.FloatField()
    sellingstr = models.CharField(max_length=100)
    rate = models.FloatField()
    time = models.TimeField()
    date = models.DateField()
    datetime = models.DateTimeField()
    calculated = models.IntegerField()


    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'coins'
        verbose_name = 'Coin'
        verbose_name_plural = "Coins"