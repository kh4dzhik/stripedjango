from django.db import models

# Create your models here.


from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)  # Связь многие-ко-многим с Item
    total_price = models.IntegerField(default=0)  # Общая стоимость заказа


    # для автоматического рассчета при сохранении заказа
    def save(self, *args, **kwargs):
        # Сначала сохраняем заказ
        super().save(*args, **kwargs)
        # Затем пересчитываем общую стоимость
        self.calculate_total_price()

    def calculate_total_price(self):
        # Используем update(), чтобы избежать рекурсии
        Order.objects.filter(id=self.id).update(
            total_price=sum(item.price for item in self.items.all())
        )

    def __str__(self):
        return f"Order {self.id}"