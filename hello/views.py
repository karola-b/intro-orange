from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def hello(request):
    return HttpResponse("Hello world!")


def hello_george(request):
    return HttpResponse(
        "<h2>Witaj <span style='color: red';>Jerzy</span>!</h2>"
    )


def hi(request):
    return render(request, 'hi.html')
