from django.shortcuts import render


def first(request):
    return render(
        request,
        'inheritance/first_template.html',
    )


def second_view(request):
    return render(
        request,
        'inheritance/second_template.html',
    )
