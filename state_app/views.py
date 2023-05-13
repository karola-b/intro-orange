from django.shortcuts import render


def set_cookie(request):
    response = render(
        request,
        'state_app/cookies.html'
    )
    response.set_cookie('ciasteczko1', 5)
    response.set_cookie('ciasteczko2', 10, max_age=45)

    return response


def show_cookies(request):
    return render(
        request,
        'state_app/show.html'
    )


def delete_cookie(request):
    response = render(
        request,
        'state_app/cookies.html',
    )
    response.delete_cookie('ciasteczko1')

    return response