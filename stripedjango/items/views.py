from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Order
from django.conf import settings

class OrderDetailView(View):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        return render(request, 'items/order_detail.html', {
            'order': order,
            'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY,
        })