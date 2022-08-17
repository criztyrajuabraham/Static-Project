from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect("logins")
    return render(request, 'logins.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        b = request.POST['firstname']
        c = request.POST['lastname']
        d = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect("register")
            elif User.objects.filter(email=d).exists():
                messages.info(request, "Email already taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, first_name=b, last_name=c, email=d,
                                                password=password)
                user.save();
                return redirect("logins")

        else:

            messages.info(request, "password not matching")
            return redirect("register")

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

