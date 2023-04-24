from django.shortcuts import render, HttpResponse


def hello(request):
    return HttpResponse("Hello, world!")


def eva(request):
    return HttpResponse("Hello, Eva!")


def name(request, data):
    return HttpResponse(f"Hello, {data}")
