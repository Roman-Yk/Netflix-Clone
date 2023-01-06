from django.shortcuts import render
from .forms import CreateUserForm
from movie_app.models import Customer
from django.contrib.auth import authenticate, login

# Create your views here.
def login_func(request):
    return render(request, "registration/login.html")

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer.objects.create(name=form.cleaned_data.get('username'), email=form.cleaned_data.get('email'), password =form.cleaned_data.get('password1'), user = user)
            auth_user = authenticate(request, username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password1'))
            login(request, auth_user)
    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request, "registration/registration.html", context)