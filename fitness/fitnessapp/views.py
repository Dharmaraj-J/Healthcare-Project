from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re
from .models import UserDetails,Workout,Goal,Leaderboard
from .forms import GoalForm,WorkoutForm,UserDetailsForm
from django.http import JsonResponse
import json

from django.contrib.auth.decorators import login_required



def index(request):
    if request.user.is_authenticated:
         return redirect("mainpage")
    return render(request,"index.html")


def loginpage(request):
    if request.user.is_authenticated:
        return redirect("mainpage")
    return render(request,"login.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect("mainpage")
    return render(request,"signup.html")



def register(request):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if request.method == 'POST':

        Username = request.POST['username']
        Email = request.POST['email']
        Password=request.POST['password']

        if not Username.isalnum():
            messages.error(request,'Error. Username Should only contain letters and numbers.')
            return redirect('signup')

        if(re.fullmatch(regex, Email)):
            pass
        else:
            messages.error(request,'Invalid Email')
      
        allusers = User.objects.all()

        for i in allusers:
            if(i.username==Username):
                messages.error(request,"User already exists")
                return redirect('signup')
            
        myuser = User.objects.create_user(Username, Email, Password)
        myuser.save()

        newuser= UserDetails(username=Username, email=Email,password=Password,)
        newuser.save()

        messages.success(request,"Your account has been successfully created")
        return redirect('loginpage')
    
    else:
        return HttpResponse('<h1>404-Error</h1>')
    

def approval(request):

    if request.method=="POST":
     
        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(request,username= loginusername, password= loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully LoggedIn")
            return redirect('mainpage')
    
        messages.error(request,"Invalid User. Please check the username and password" )
        return redirect("loginpage")

@login_required(login_url='loginpage') 
def mainpage(request):
    username = request.user.username
    return render(request,"mainpage.html",{ 'username':username}) 


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('loginpage')

@login_required(login_url='loginpage') 
def running(request):
   username = request.user.username
   return render(request, "running.html",{'username':username})

@login_required(login_url='loginpage') 
def cycling(request):
   username = request.user.username
   return render(request, "cycling.html",{ 'username':username})

@login_required(login_url='loginpage') 
def swimming(request):
   username = request.user.username
   return render(request, "swimming.html",{ 'username':username})

@login_required(login_url='loginpage') 
def gym(request):
   username = request.user.username
   return render(request, "gym.html",{ 'username':username})

@login_required(login_url='loginpage') 
def userview(request):
   profile = UserDetails.objects.get(username=request.user)
   return render(request, "userview.html",{ 'profile' : profile })

def update_leaderboard(request):
    if request.method == 'POST'and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        points = request.POST.get('value')
        data = json.loads(request.body)
        value = data.get('value')
        print(value)
        # activity = request.POST['value']
        # print(activity)
        print(points)
        user = request.user
        leaderboard, created = Leaderboard.objects.get_or_create(user=user)
        print(leaderboard)
        leaderboard.points += 1
        leaderboard.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})



def leaderboard_view(request):
    leaderboard = Leaderboard.objects.all().order_by( '-points')
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard})


def set_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            # messages.success(request, 'Goal set successfully!')
            return redirect('set_goal')
    else:
        form = GoalForm()
        username = request.user.username
        usergoals = Goal.objects.filter(user__username=username)
    return render(request, 'set_goal.html', {'form': form,'usergoals':usergoals})


def generate_report(request):
    return render(request, 'generate_report.html')


def record_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            # messages.success(request, 'Workout recorded successfully!')
            return redirect('record_workout')
    else:
        form = WorkoutForm()
        allactivity = Workout.objects.all()
    return render(request, 'record_workout.html', {'form': form,'allactivity':allactivity})

@login_required(login_url='loginpage') 
def editprofile(request,pk):
    user_details_instance = UserDetails.objects.get(pk=pk)
    form = UserDetailsForm(instance=user_details_instance)
    
    return render(request, "edit.html", {'form': form})