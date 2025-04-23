from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
# Create your views here.

fake_users = {
    "1":{"id":1,"name":"saqiba"},
    "2":{"id":2,"name":"juna"}
}


@api_view(["GET","POST"])
def get_user(request,user_id):
    # return Response("Hello world")        
    
    return Response(
        fake_users.get(user_id, {"error":"not found"})
    )
        
    