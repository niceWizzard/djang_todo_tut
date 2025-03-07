from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register_page(req : HttpRequest):
    return render(req, template_name='users/register.html')

def login_page(req : HttpRequest):
    form = AuthenticationForm()
    if req.method == "POST":
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            return redirect('/')
    return render(req, template_name='users/login.html', context={'form': form})

def users_page(req: HttpRequest):
    return HttpResponse("HELLO")