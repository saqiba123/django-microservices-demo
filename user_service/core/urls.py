from django.urls import path
from .views import get_user

urlpatterns = [
    path('user/<str:user_id>/', get_user, name="user"),
]
