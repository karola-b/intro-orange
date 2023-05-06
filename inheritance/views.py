from django.shortcuts import render


def first(request):
    return render(
        request,
        'inheritance/first_template.html',
    )
