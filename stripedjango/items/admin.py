from django.contrib import admin
from .models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price')
    filter_horizontal = ('items',)  # Горизонтальный виджет для выбора товаров

    def save_model(self, request, obj, form, change):
        # Сначала сохраняем заказ
        super().save_model(request, obj, form, change)
        # Затем добавляем товары и пересчитываем общую стоимость
        obj.calculate_total_price()