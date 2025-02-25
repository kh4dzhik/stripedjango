from django.urls import path
from .views import BuyOrderView

urlpatterns = [
    path('order/<int:id>/', BuyOrderView.as_view(), name='buy_order'), # or buy/order/id
]