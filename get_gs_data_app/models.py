from django.db import models


class SheetsData(models.Model):
    order_num = models.BigIntegerField(blank=False)
    cost_dol = models.IntegerField(blank=False)
    cost_rub = models.IntegerField(blank=False)
    delivery_time = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return f'{self.order_num}'