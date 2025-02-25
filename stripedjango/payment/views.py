from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from items.models import Order
import stripe
from django.conf import settings

class BuyOrderView(View):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        line_items = []

        # все продукты заказа в понятную для Stripe структуру
        for item in order.items.all():
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            })


        # создаем сессию Stripe с продуктами
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url='http://localhost:8000/success/',
            cancel_url='http://localhost:8000/cancel/',
        )

        """запрос отправил JS в котором иничиализирован Stripe нам достаточно вернуть session_id,
         фронт сам перенаправит нас на страницу платежа"""
        return JsonResponse({'session_id': session.id})