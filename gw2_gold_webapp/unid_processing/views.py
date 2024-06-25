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
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import CustomUser
from . serializer import CustomUser_Serializer
# Create your views here.

def data_dump_view(request):
    """
    This function is testing out dumping data into local text file

    1.) pull data from API
    2.) Create a file with the data
    3.) Save the file to local
    """
    
    response = HttpResponse(headers={"Content-Type": "text/plain",
                                     "Content-Disposition": 'attachment; filename="test.txt"'},)
    
    lines = ["This is line 1\n",
            "This is line 2\n",
            "this is line 3\n"]
    
    response.writelines(lines)
    return response

class CustomUser_List_ViewSet(generics.ListAPIView):
    """
    This view allows those with the correct permissions to view users.
    TODO: Allow only managers to view user list
    """
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUser_Serializer


class CustomUser_Create_ViewSet(generics.CreateAPIView):
    """
    This view allows users to register a new account.
    """
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUser_Serializer



