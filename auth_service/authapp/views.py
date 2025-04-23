from django.shortcuts import render

# Create your views here.
import jwt
from rest_framework.decorators import api_view
from rest_framework.response import Response

SECRET_KEY="saqiba"

@api_view(["GET"])
# def login(request,user_id):
#     token = jwt.encode({"user_id":user_id},SECRET_KEY,algorithm="HS256")
#     return Response({"token":token})

def login(request):
    user_id = request.GET.get('user_id')
    if not user_id:
        return Response({"error": "user_id is required"}, status=400)
    
    token = jwt.encode({"user_id": user_id}, SECRET_KEY, algorithm="HS256")
    return Response({"token": token})

@api_view(['GET'])
def verify(request):
    token = request.GET.get('token')
    try:
        data = jwt.decode(token,SECRET_KEY,algorithms="HS256")
        return Response({"valid":True,'data':data})
    except:
        return Response({"valid":False})
