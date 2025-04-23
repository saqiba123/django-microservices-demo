from django.urls import path
from .views import place_order


urlpatterns = [
    path('order/<str:user_id>/',place_order,name="order")
]
