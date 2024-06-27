from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics, viewsets
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import CustomUser
from . serializer import CustomUser_Serializer
# Create your views here.

class CustomUser_List_ViewSet(generics.ListAPIView):
    """
    This view allows admin to viewa list of all users.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUser_Serializer

def GW2_Items_Create_View(request):
    """
    This view allows for creation of new objects in GW2_Items, update current items, and delete current items.
    """
    pass