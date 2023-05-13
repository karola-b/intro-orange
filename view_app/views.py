from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

from django import views
from django.views.generic import TemplateView

def hello(request):
    return HttpResponse("Hello, world!")


class HelloView(views.View):
    def get(self, request):
        return HttpResponse("Hello, world!")


# function view
def hello_function_view(request):
    return render(
        request,
        'view_app/hello.html',
    )


# class view
class HelloClassView(views.View):
    def get(self, request):
        return render(
            request,
            'view_app/hello.html',
        )


# generic class view
class HelloGenericView(views.generic.TemplateView):
    template_name = 'view_app/hello.html'
