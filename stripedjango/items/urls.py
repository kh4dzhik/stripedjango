from django.urls import path
from .views import OrderDetailView


urlpatterns = [
    path('order/<int:id>/', OrderDetailView.as_view(), name='order_detail'),
]