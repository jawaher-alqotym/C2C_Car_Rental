
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import *
from .models import *

@api_view(['POST'])
def register(request: Request):
    '''
    A register method for user
    '''
    User_serializer = UserSerializer(data=request.data)

    if User_serializer.is_valid():
        User_serializer.save()
        return Response({"msg": "New user hase been created"})
    else:
        print(User_serializer.errors)
        return Response({"msg": "Couldn't create a user"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request: Request):
    '''
    A method fo log in
    '''
    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user:
            token = AccessToken.for_user(user)
            responseData = {
                "msg": "Your token have been generated",
                "token": str(token)
            }
            return Response(responseData)
