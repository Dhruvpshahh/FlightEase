from os import environ
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from authentication.models import Request
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import ExtractMonth
import calendar

from django.http import JsonResponse
from .models import Booking, Passenger


from authentication.models import Flight,Booking
from datetime import datetime, timedelta
import random
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def profile_view(request):
    if request.user.is_authenticated:  
        user = request.user
        if request.method == 'POST':
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            
            if username:
                user.username = username
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if email:
                user.email = email
            
            user.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('signin')
        
        return render(request, 'authentication/profile.html', {'user': user})
    else:
        return redirect('signin')

def signup(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensuring password matches confirmation
        password = request.POST["pass1"]
        confirmation = request.POST["pass2"]
        if password != confirmation:
            return render(request, "authentication/signup.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
        except:
            return render(request, "authentication/signup.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect('book')

    else:
        return render(request, "authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass1"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book')

            
        else:
            return render(request, "authentication/signin.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if request.user.is_authenticated:
            return redirect('book')

        else:
            return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse("signin"))
