from django.db import models
from utils.models import BaseModel


class Coin(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    buying = models.IntegerField()
    buying_str = models.CharField(max_length=50)
    selling = models.IntegerField()
    selling_str = models.CharField(max_length=50)
    rate = models.IntegerField()
    time = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    datetime = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'coins'
        verbose_name = 'Coin'
        verbose_name_plural = "Coins"