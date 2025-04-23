from django.urls import path, include
from .views import verify, login


# urlpatterns = [
#     path('login/<str:user_id>/',login,name="login"),
#     path('verify/', verify,name="verify")
# ]

urlpatterns = [
    path('users/login/', login, name="login"),   # query param is handled inside the view
    path('users/verify/', verify, name="verify"),
]