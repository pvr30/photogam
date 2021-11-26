from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


# authentication views
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        profile_pic = request.FILES['profile_pic']
        bio = request.POST['bio']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password == confirm_password:
            # check if username already exists or not
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'username already exists')
                return redirect("signup")
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'email already exists')
                    return redirect("signup")
                else:
                    user = User.objects.create_user(username=username,phone=phone,
                                                email=email, profile_pic=profile_pic, bio=bio, password=password)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect("login")
                   


    return render(request, "accounts/signup.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=username, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'you are logged in...')
            return redirect('home')
        else:
            messages.warning(request, 'invalid crendentials')
            return redirect('login')

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')



