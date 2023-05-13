from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()


def index(request):
    users = User.objects.all()
    print(users)

    # User.objects.create_user(username='test4', password='tajne')

    user = authenticate(username='admin', password='admin')

    if user:
        login(request, user=user)

    logout(request)

    return render(
        request,
        'auth_app/index.html'
    )


def login_view(request):
    if request.method == "GET":
        print(request.user)
        return render(
            request,
            'auth_app/login.html'
        )
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user=user)

        return redirect('auth_app:login')


def logout_view(request):
    logout(request)

    return redirect('auth_app:login')

