from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CreateUserForm
from movie_app.models import Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_func(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            print("user does not exist")
    
    return render(request, "registration/login.html")

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer.objects.create(name=form.cleaned_data.get('username'), email=form.cleaned_data.get('email'), password =form.cleaned_data.get('password1'), user=user)
            auth_user = authenticate(request, username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password1'))
            login(request, auth_user)
            return redirect('homepage')
    else:
        form = CreateUserForm()
    
    context = {'form':form}
    return render(request, "registration/registration.html", context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('homepage')