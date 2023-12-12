from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def start(request):
    return render(request, 'intro.html')
# Create your views here.


def about_us(request):
    print('you are ', request.session.get('username'))
    return render(request, 'about-us.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = auth.authenticate( username=username, password=password)

        if user is not None:
            auth.login(request, user)

            request.session['user_id'] = user.id
            request.session['username'] = user.username

            return redirect('/products')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already Taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already Taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                print('user created')
                return redirect('/login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('/register')

    else:
        return render(request, 'register.html')



