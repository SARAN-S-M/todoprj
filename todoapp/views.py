from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'todoapp/todo.html', {})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username') #the data will came as a json type so specify the attribute name that you have gave in the html file name tag for each field
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(username, email, password)

        if len(password) < 3:
            messages.error(request, 'Password is too short..')
            return redirect('register')

        get_all_users_by_username = User.objects.filter(username = username)
        if get_all_users_by_username:
            messages.error(request, 'Username is already taken..')
            return redirect('register')
        
        new_user = User.objects.create_user(username = username, email = email, password = password)
        new_user.save()
        messages.success(request, 'Account created successfully..')
        return redirect('login')

    return render(request, 'todoapp/register.html', {})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password = password) # it return user object if user exists therwise return none
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')
        else:
            messages.error(request, 'Invalid credentials..')
            return redirect('login')
        
    return render(request, 'todoapp/login.html', {})