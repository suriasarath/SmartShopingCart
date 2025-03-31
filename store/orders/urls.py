from django.urls import path
from . import views 

app_name = 'orders'

urlpatterns = [
    path('', views.payment_method, name='payment_method'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('payments/', views.payments, name='payments'),
    path('order_completed/', views.order_completed, name='order_complete'),
    path('order_complete/<slug:order>', views.order_completed1, name='order_complete'),
    path('return/<slug:order>', views.return_order, name='order_complete'),
    
]
