from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .forms import UsterCreationForm
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

def register_page(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form= UserCreationForm(request.POST)