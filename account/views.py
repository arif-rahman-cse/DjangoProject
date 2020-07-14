from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        pass1 = request.POST['psw']
        pass2 = request.POST['psw-repeat']

        if(pass1 == pass2):

            if User.objects.filter(username=username).exists():
                print('User name alredy Exists !')
                messages.info(request, 'User name alredy Exists !')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                print('Email already Exists !')
                messages.info(request, 'Email already Exists !')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username, password=pass1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        else:
            print('Password not matching !')
            messages.info(request, 'Password not maching ! ')
            return redirect('register')

        return redirect('/')

    else:
        return render(request, 'register.html')
