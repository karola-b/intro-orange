from django.shortcuts import render, HttpResponse
from django.utils.html import escape


def hello(request):
    return HttpResponse("Hello, world!")


def eva(request):
    return HttpResponse("Hello, <span style='color:red'>Eva<span/> !")


def name(request, data):
    escaped_data = escape(data)
    return HttpResponse(f"Hello, {escaped_data}")


def hello2(request):
    return render(
        request,
        'hello.html'
    )


def name2(request, data):
    return render(
        request,
        'name.html',
        context={
            "data": data
        }
    )
