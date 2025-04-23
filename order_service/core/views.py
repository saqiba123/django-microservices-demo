from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def place_order(request,user_id):
    user = requests.get(f"http://localhost:8002/user/{user_id}").json()
    token = requests.get(f"http://localhost:8001/users/login?user_id={user_id}").json()
    
    return Response({
        "user":user,
        "token":token["token"],
        "order_status":"created"
    })
    
