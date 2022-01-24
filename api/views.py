from lib2to3.pgen2 import token
from multiprocessing import AuthenticationError
from unittest import result
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from api.models import Owner, Properties
from rest_framework import generics
from api.serializers import SerializerOwner, SerializerProperties, SerializerUserLogin, SerializerUserRegister
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Login(APIView):

    def post(self, request, format=None):
        serializer = SerializerUserLogin(data= request.data)
        serializer.is_valid(raise_exception=True)
        user,token=serializer.save()
        data = {
            'user':user.id,
            'token':token.key 
        }
        return Response(data)
    
class Register(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = SerializerUserRegister(data= request.data)
        serializer.is_valid(raise_exception=True)
        
        result = serializer.save()
        
        return Response('sucess')
    
    
class OwnerCreate(generics.CreateAPIView):
    serializer_class = SerializerOwner
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Owner.objects.all()
    
class OwnerList(generics.ListAPIView):
    serializer_class = SerializerOwner
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Owner.objects.all()
    
    
    
class PropertiesCreate(generics.CreateAPIView):
    serializer_class = SerializerProperties
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Properties.objects.all()
    
class PropertiesList(generics.ListAPIView):
    serializer_class = SerializerProperties
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Properties.objects.all()
 
 