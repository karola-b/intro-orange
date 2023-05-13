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
        'state_app/show_cookies.html'
    )


def delete_cookie(request):
    response = render(
        request,
        'state_app/cookies.html',
    )
    response.delete_cookie('ciasteczko1')

    return response


def set_session(request):
    request.session['num_visit'] = 0
    return render(
        request,
        'state_app/session.html'
    )


def show_session(request):
    num_visit = request.session.get('num_visit')
    return render(
        request,
        'state_app/show_session.html',
        context={
            'num_visit': num_visit,
        }
    )


def update_session(request):
    num_visit = request.session.get('num_visit', 0)
    request.session['num_visit'] = num_visit + 1

    return render(
        request,
        'state_app/show_session.html',
        context={
            'num_visit': request.session.get('num_visit')
        }
    )


def delete_session(request):
    del request.session['num_visit']

    return render(
        request,
        'state_app/session.html'
    )