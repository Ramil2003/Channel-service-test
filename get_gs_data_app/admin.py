from django.contrib import admin

from .models import SheetsData


@admin.register(SheetsData)
class SheetsDataAdmin(admin.ModelAdmin):
    readonly_fields = ('order_num', 'cost_dol', 'cost_rub', 'delivery_time',)
