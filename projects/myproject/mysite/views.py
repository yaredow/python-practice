# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("Hello world!".encode("utf-8"))
    return render(request, "home.html")


def about(request):
    # return HttpResponse("This is the about page".encode("utf-8"))
    return render(request, "about.html")
