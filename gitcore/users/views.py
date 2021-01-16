from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
