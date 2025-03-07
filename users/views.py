from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def register_page(req : HttpRequest):
    return render(req, template_name='users/register.html')

def login_page(req : HttpRequest):
    return render(req, template_name='users/login.html')

def users_page(req: HttpRequest):
    return HttpResponse("HELLO")