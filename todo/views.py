from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def homepage(request : HttpRequest ) -> HttpResponse:
    # return HttpResponse("Hello World!")
    return render(request, 'home.html')
