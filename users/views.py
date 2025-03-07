from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, login

# Create your views here.
def register_page(req : HttpRequest):
    form = UserCreationForm()
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            return redirect("/")
    return render(req, template_name='users/register.html',context={'form': form})

def login_page(req : HttpRequest):
    form = AuthenticationForm()
    if req.method == "POST":
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            login(req, user=form.get_user())
            return redirect('/')
    return render(req, template_name='users/login.html', context={'form': form})

def users_page(req: HttpRequest):
    return HttpResponse("HELLO")

def logout_call(req:HttpRequest):
    if req.method == "POST":
        logout(req)
        return redirect('/')